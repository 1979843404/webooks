# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
import sources

class SourceFactory(object):
    @classmethod
    def get_source(cls, name):
        cls_name = "Source%s" %name
        source_cls = getattr(sources, cls_name, None)
        return source_cls()