# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models
from webooks.utils import const
from webooks.utils.alias import tran_lazy as _
from webooks.utils.util import now
from webooks.models.mixins import GetByUniqueMixin
from django.db.models import Q

class Strategy(models.Model, GetByUniqueMixin):
    class Meta:
        app_label = 'webooks'
        db_table = 'webooks_strategy'
        verbose_name = verbose_name_plural = _('更新策略')

    name = models.CharField(_('名字'), max_length=const.DB_NAME_LENGTH, blank=True, null=True)
    type = models.SmallIntegerField(_('更新策略'), choices=const.UPDATE_STRATEGY_CHOICES,
        default=const.UPDATE_BY_TIME, blank=True, null=True)
    data = models.CharField(_('具体策略'),max_length=const.DB_MIDDLE_LENGTH, blank=True, null=True)

    def __unicode__(self):
        return "%s : %s" % (self.name, self.data)

    @classmethod
    def get_times(cls, time=now().time()):
        """
        目前先做小时级别的更新，通过data做模糊匹配，取出strategy_id, 反查需要更新的books
        """
        hour = time.strftime("%H")
        result = "%s:00" %hour
        return [result, ]

    @classmethod
    def get_time_strategies(cls, times):
        query = Q(type=const.UPDATE_BY_TIME)
        for time in times:
            query |= Q(data__icontains=time)

        return cls.objects.all().filter(query)