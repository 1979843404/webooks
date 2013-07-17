# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models
from webooks.utils.alias import tran_lazy as _
from webooks.models import Book, Account
from django.utils.timezone import now

class Collect(models.Model):
    class Meta:
        app_label = 'webooks'
        db_table = 'webooks_collect'
        verbose_name = verbose_name_plural = _('收藏')

    account = models.ForeignKey(Account, verbose_name=_("用户id"))
    book = models.ForeignKey(Book, verbose_name=_("书"))
    datetime = models.DateTimeField(_("收藏时间"), default=now)

