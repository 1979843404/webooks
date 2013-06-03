# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models
from webooks.utils.alias import tran_lazy as _
from webooks.utils import const

class Tag(models.Model):
    class Meta:
        app_label = 'webooks'
        db_table = "webooks_tag"
        verbose_name = verbose_name_plural = _('标签')

    name = models.CharField(_(u'名字'), max_length=const.DB_NAME_LENGTH, unique=True)

    def __unicode__(self):
        return self.name