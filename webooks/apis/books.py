# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from rest_framework import viewsets
from webooks.models import Book, Chapter

class BookViewSet(viewsets.ModelViewSet):
    model = Book

class ChapterViewSet(viewsets.ModelViewSet):
    model = Chapter

