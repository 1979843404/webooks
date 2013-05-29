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

    number = models.IntegerField(_(u'章节号'), default=const.DB_NUMBER_DEFAULT)
    book = models.ForeignKey(Book, verbose_name=_('书'))
    content = models.TextField(_(u'内容'), max_length=const.DB_CONTENT_LENGTH)