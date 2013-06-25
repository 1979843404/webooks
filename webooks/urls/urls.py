# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from webooks.views.books import BookList, ChapterList, ChapterView, BookDetailView
from rest_framework.urlpatterns import format_suffix_patterns
from webooks.utils import const

urlpatterns = patterns('',
    url("^books/$", BookList.as_view(), name="book_list"),
    url("^books/%s/$" % const.URL_BOOK_ID, BookDetailView.as_view(), name="book_detail"),
    url("^books/%s/chapters/$" % const.URL_BOOK_ID, ChapterList.as_view(), name="book_chapters"),
    url("^books/%s/chapters/%s/$" %(const.URL_BOOK_ID, const.URL_CHAPTER_ID), ChapterView.as_view(),
        name="chapter_detail")
)

urlpatterns = format_suffix_patterns(urlpatterns)