# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from webooks.utils import const
from webooks.views.books import BookDetailView

urlpatterns = patterns('',
    url(r'^books/%s/' %const.URL_ID, BookDetailView.as_view(),name="book_detail"),
)

urlpatterns = format_suffix_patterns(urlpatterns)