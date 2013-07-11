# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models
from webooks.utils.alias import tran_lazy as _
from webooks.utils import const
from webooks.models import Book, Chapter

class History(models.Model):
    class Meta:
        app_label = 'webooks'
        db_table = 'webooks_history'
        verbose_name = verbose_name_plural = _('阅读历史')

    user_id = models.CharField(_("用户id"), max_length=const.DB_NAME_LENGTH)
    book = models.ForeignKey(Book, verbose_name=_("书"))
    chapter = models.ForeignKey(Chapter, verbose_name=_("章节"), blank=True, null=True)
