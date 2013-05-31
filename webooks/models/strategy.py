# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models
from webooks.utils import const
from webooks.utils.alias import tran_lazy as _

class Strategy(models.Model):
    class Meta:
        app_label = 'webooks'
        db_table = 'webooks_strategy'
        verbose_name = verbose_name_plural = _('更新策略')

    name = models.CharField(_('名字'), max_length=const.DB_NAME_LENGTH, blank=True, null=True)
