# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from views import interface

urlpatterns = patterns("",
    url(r'^interface/$', interface, name="wx_interface")
)

urlpatterns = format_suffix_patterns(urlpatterns)