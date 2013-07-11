# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models
from webooks.utils.alias import tran_lazy as _
from webooks.utils import const
from webooks.models import Book
from django.utils.timezone import now

class Collect(models.Model):
    class Meta:
        app_label = 'webooks'
        db_table = 'webooks_collect'
        verbose_name = verbose_name_plural = _('收藏')

    user_id = models.CharField(_("用户id"), max_length=const.DB_NAME_LENGTH)
    book = models.ForeignKey(Book, verbose_name=_("书"))
    datetime = models.DateTimeField(_("收藏时间"), default=now)
