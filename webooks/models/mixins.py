# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db.models import Q

class AutoRedisMixin(object):
    def get_cache_key(self):
        return self.__class__.get_cache_by_id(id)

    def to_json(self):
        raise NotImplemented

    def to_cache(self):
        key = self.get_cache_key()
        # set redis
        # redis.hset(key, self.to_json)

    def clear_cache(self):
        key = self.get_cache_key()
        # delete cache
        # redis.delete(key)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(AutoRedisMixin, self).save(force_insert=force_insert,
            force_update=force_update, using=using, update_fields=update_fields)
        self.to_cache()

    @classmethod
    def get_cache_key_by_id(cls, id):
        key = "%s:%d" % (cls.__name__, id)
        return key

    @classmethod
    def get_cache_by_id(cls, id):
        key = cls.get_cache_by_id(id)
        json_data = {} # redis.hget(key)
        if not json_data:
            item = cls.objects.get(id=id)
            item.to_cache()
            json_data = item.to_json()

        # json_data 最好用DottedDict，需要自己实现
        return json_data

class GetByUniqueMixin(object):
    @classmethod
    def get_by_unique(cls, **kwargs):
        try:
            instance = cls.objects.get(**kwargs)
        except:
            instance = None
        return instance

    @classmethod
    def get_by_queries(cls, **kwargs):
        query_list = [Q(**{key: value}) for key, value in kwargs.items()]
        query = query_list.pop()
        for query_append in query_list:
            query &= query_append

        try:
            item = cls.objects.get(query)
        except Exception:
            item = None
        return item

    @classmethod
    def filter_by_queries(cls, **kwargs):
        query_list = [Q(**{key: value}) for key, value in kwargs.items()]
        query = query_list.pop()
        for query_append in query_list:
            query &= query_append

        try:
            item = cls.objects.filter(query)
        except Exception:
            item = None
        return item


class GetOrCreateMixin(object):
    pass