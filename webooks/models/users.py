# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from webooks.utils.alias import tran_lazy as _
from webooks.utils import const
from django.db import models

class Account(models.Model):
    class Meta:
        app_label = 'webooks'
        verbose_name = verbose_name_plural = _('账号')
        unique_together = ("id", "src_from")

    id = models.CharField(_("账号id"), max_length=const.DB_NAME_LENGTH, primary_key=True)
    src_from = models.SmallIntegerField(_("来源"), choices=const.THIRD_FROM_CHOICES,
        default=const.FROM_LOCAL_KEY)

    def __unicode__(self):
        return u"%s: %s" % (self.get_src_from_display(), self.src_from)

    @property
    def third(self):
        third_from_display = self.get_src_from_display()
        if third_from_display == "local":
            return None
        else:
            return getattr(self, third_from_display)

class WeiXin(Account):
    class Meta:
        app_label = 'webooks'
        verbose_name = verbose_name_plural = _('微信账号')

    def __unicode__(self):
        return u"微信: %s" % self.id

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.src_from = const.FROM_WEIXIN_KEY
        super(WeiXin, self).save(force_insert, force_update, using, update_fields)
