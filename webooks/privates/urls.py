# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url("^books/$", views.books, name="internal_api_books"),
    url("^chapter/$", views.chapter, name="internal_api_chapter"),
    url("^chapters/$", views.chapters, name="internal_api_chapters"),
)