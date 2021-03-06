# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models
from django.utils.timezone import now
from webooks.models.mixins import GetByUniqueMixin
from webooks.utils.alias import tran_lazy as _
from webooks.models import Book, Chapter, Account

class History(models.Model, GetByUniqueMixin):
    class Meta:
        app_label = 'webooks'
        db_table = 'webooks_history'
        verbose_name = verbose_name_plural = _('阅读历史')
        ordering = ["datetime"]

    account = models.ForeignKey(Account, verbose_name=_("账号"))
    book = models.ForeignKey(Book, verbose_name=_("书"))
    chapter = models.ForeignKey(Chapter, verbose_name=_("章节"), blank=True, null=True)
    datetime = models.DateTimeField(_("阅读时间"), default=now, blank=True, null=True)

    def __unicode__(self):
        return "%s: %s" %(self.book.name, self.chapter.title)

    @classmethod
    def update_or_create(cls, account_id, book_id, chapter_id=""):
        queries = {
            "account_id": account_id,
            "book_id": book_id
        }
        item = cls.get_by_queries(**queries)
        if not item:
            item = cls(account_id=account_id, book_id=book_id, chapter_id=chapter_id)
        else:
            item.chapter_id = chapter_id
        item.datetime = now()
        item.save()

