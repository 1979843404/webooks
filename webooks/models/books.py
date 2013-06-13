# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from webooks.utils.alias import tran_lazy as _
from django.db import models
from django.db.models import Q
from webooks.utils import const
from webooks.models.tags import Tag
from webooks.utils.util import number2chinese
from webooks.models.mixins import GetByUniqueMixin

class Book(models.Model, GetByUniqueMixin):
    class Meta:
        app_label = 'webooks'
        db_table = 'webooks_book'
        verbose_name = verbose_name_plural = _('书')

    name = models.CharField(_(u'书名'), max_length=const.DB_NAME_LENGTH)
    tags = models.ManyToManyField(Tag, verbose_name=_('标签'), blank=True, null=True,
        through='BookTagShip', related_name='books')
    is_over = models.BooleanField(_(u'是否完结'), default=False)
    author = models.CharField(_(u'作者'), max_length=const.DB_NAME_LENGTH, default="", blank=True, null=True)
    description = models.CharField(_(u'描述'), max_length=const.DB_DESCRIPTION_LENGTH,
        default="", blank=True, null=True)
    score = models.BigIntegerField(_(u'评分'), default=0, blank=True, null=True)
   # lock = models.BooleanField(_(u'锁定'), default=False, blank=True, null=True)

    def __unicode__(self):
        return self.name

    @classmethod
    def get_or_create(cls, name, **kwargs):
        item = cls.get_by_unique(name=name)
        if not item:
            item = cls(name=name, **kwargs)
            item.save()
        return item

    def to_txt(self, path):
        if not path.endswith("txt"):
            path = "%s.txt" % path

        file_handle = open(path, "w")
        chapters = self.chapter_set.all()
        for chapter in chapters:
            pages = chapter.page_set.all()
            title = unicode(chapter).encode('utf-8')
            file_handle.write(title)
            for page in pages:
                content = page.content
                file_handle.write(content.encode('utf-8'))
        file_handle.close()

class BookTagShip(models.Model, GetByUniqueMixin):
    class Meta:
        app_label = "webooks"
        db_table = "webooks_book_tag_ship"
        verbose_name = verbose_name_plural = _('书与标签')

    book = models.ForeignKey(Book)
    tag = models.ForeignKey(Tag)

    def __unicode__(self):
        return "%s: %s" %(self.book.name, self.tag.name)

class Chapter(models.Model, GetByUniqueMixin):
    class Meta:
        app_label = 'webooks'
        db_table = 'webooks_chapter'
        verbose_name = verbose_name_plural = _('章节')
        ordering = ['number']

    name = models.CharField(_(u'名字'), max_length=const.DB_NAME_LENGTH,
        default="", blank=True, null=True)
    number = models.IntegerField(_(u'章节号'), default=const.DB_NUMBER_DEFAULT)
    book = models.ForeignKey(Book, verbose_name=_('书'))
    #lock = models.BooleanField(_(u'锁定'), default=False, blank=True, null=True)

    def __unicode__(self):
        return "%s_%d章" % (self.book.name, self.number)

    def full_content(self):
        pages = self.page_set.all()
        content = ""
        for page in pages:
            content += page.content
            content += "\n"
        return content

    @classmethod
    def get_or_create(cls, book, number, **kwargs):
        item = cls.get_by_queries(book=book, number=number)
        if not item:
            item = cls(book=book, number=number, **kwargs)
            item.save()
        return item

class Page(models.Model, GetByUniqueMixin):
    class Meta:
        app_label = 'webooks'
        db_table = 'webooks_page'
        verbose_name = verbose_name_plural = _('页码')
        ordering = ['number']

    number = models.IntegerField(_(u'页数'), default=const.DB_NUMBER_DEFAULT)
    chapter = models.ForeignKey(Chapter, verbose_name=_(u'章节'))
    content = models.TextField(_(u'内容'), max_length=const.DB_CONTENT_LENGTH)
    #lock = models.BooleanField(_(u'锁定'), default=False, blank=True, null=True)

    def __unicode__(self):
        return "%s_%d页" % (self.chapter, self.number)

    @classmethod
    def get_or_create(cls, number, chapter, **kwargs):
        item = cls.get_by_queries(number=number, chapter=chapter)
        if not item:
            item = cls(number=number, chapter=chapter, **kwargs)
            item.save()
        return item