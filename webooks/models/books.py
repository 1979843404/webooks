# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from webooks.utils.alias import tran_lazy as _
from django.db import models
from webooks.utils import const
from webooks.models.tags import Tag
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
    lock = models.BooleanField(_(u'锁定'), default=False)

    src_name = models.CharField(_(u'来源名'), max_length=const.DB_SHORT_LENGTH, blank=True, null=True, default="")
    src_id = models.CharField(_(u'来源id'), max_length=const.DB_MIDDLE_LENGTH, blank=True, null=True, default="")
    src_url = models.CharField(_(u'来源URL'), max_length=const.DB_URL_LENGTH, blank=True, null=True, default="")

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

    title = models.CharField(_(u'章节名'), max_length=const.DB_NAME_LENGTH,
        default="", blank=True, null=True)
    number = models.IntegerField(_(u'章节号'), default=const.DB_NUMBER_DEFAULT)
    book = models.ForeignKey(Book, verbose_name=_('书'))
    lock = models.BooleanField(_(u'锁定'), default=False)
    content = models.TextField(_(u'内容'), default="", max_length=const.DB_CONTENT_LENGTH)

    src_url = models.CharField(_(u'来源URL'), max_length=const.DB_URL_LENGTH, blank=True, null=True, default="")

    def __unicode__(self):
        return "%s" %self.title

    def full_content(self):
        return self.content

    @classmethod
    def get_or_create(cls, book, number, **kwargs):
        item = cls.get_by_queries(book=book, number=number)
        if not item:
            item = cls(book=book, number=number, **kwargs)
            item.save()
        return

    def lazy_loading(self):
        from webooks.middles import SourceFactory

        src = self.book.src_name
        source = SourceFactory.get_source(src)
        source.get_chapter_content(self)