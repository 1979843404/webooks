# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db.models import Q

class GetByUniqueMixin(object):
    @classmethod
    def get_by_unique(cls, **kwargs):
        try:
            instance = cls.objects.get(**kwargs)
        except:
            instance = NotImplemented
        return instance

class GetOrCreateMixin(object):
    pass