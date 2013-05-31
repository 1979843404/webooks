# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from webooks.utils.alias import tran_lazy as _
from django.db import models
from webooks.utils import const
from webooks.models.tags import Tag

class Book(models.Model):
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

    def __unicode__(self):
        return self.name

class BookTagShip(models.Model):
    class Meta:
        app_label = "webooks"
        db_table = "webooks_book_tag_ship"
        verbose_name = verbose_name_plural = _('书与标签')

    book = models.ForeignKey(Book)
    tag = models.ForeignKey(Tag)

class Chapter(models.Model):
    class Meta:
        app_label = 'webooks'
        db_table = 'webooks_chapter'
        verbose_name = verbose_name_plural = _('章节')
        ordering = ['-number']

    number = models.IntegerField(_(u'章节号'), default=const.DB_NUMBER_DEFAULT)
    book = models.ForeignKey(Book, verbose_name=_('书'))

class Page(models.Model):
    number = models.IntegerField(_(u'页数'), default=const.DB_NUMBER_DEFAULT)
    chapter = models.ForeignKey(Chapter, verbose_name=_(u'章节'))
    content = models.TextField(_(u'内容'), max_length=const.DB_CONTENT_LENGTH)