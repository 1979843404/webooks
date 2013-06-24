# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

class SourceInterface(object):
    spider = None

    def get_all_books(self):
        raise NotImplemented

    def get_chapters(self, book, *args, **kwargs):
        raise NotImplemented

    def get_chapter_content(self, book, *args, **kwargs):
        raise NotImplemented

