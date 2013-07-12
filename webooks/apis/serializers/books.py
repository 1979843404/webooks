# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from rest_framework import serializers
from webooks.models import Book, Chapter
from webooks.utils import const

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "name", "author", "description", "api_url")

    api_url = serializers.CharField(max_length=const.DB_URL_LENGTH, default="")

class ChapterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ("id", "title", "book")

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book

class ChapterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ("id", "title", "book", "content", "before", "after")

    before = serializers.CharField(max_length=const.DB_URL_LENGTH, default="")
    after = serializers.CharField(max_length=const.DB_URL_LENGTH, default="")