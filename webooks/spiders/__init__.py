# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from zhangbook import ZBSpider as ZhangBook
__all__ = [ZhangBook, ]

class SpiderFactory(object):
    mapping = dict(map(lambda cls: (cls.__name__, cls), __all__))

    @classmethod
    def get_spider(cls, name):
        if name not in cls.mapping:
            raise Exception
        else:
            return cls.mapping[name]()