# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from books import Book, Chapter

class BookService(object):
    @classmethod
    def get_or_create(cls, queries, *args, **kwargs):
        item = Book.get_by_queries(**queries)
        if not item:
            item = Book(*args, **kwargs)
            item.save()
        return item

class ChapterService(object):
    @classmethod
    def get_or_create(cls, queries, *args, **kwargs):
        item = Chapter.get_by_queries(**queries)
        if not item:
            item = Chapter(*args, **kwargs)
            item.save()
        return item

    @classmethod
    def update(cls, queries, **kwargs):
        items = Chapter.filter_by_queries(**queries)
        if not items:
            return
        else:
            items.update(**kwargs)