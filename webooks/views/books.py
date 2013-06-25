# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from webooks.models import Book, Chapter
from webooks.apis.serializers.books import (BookSerializer,
    ChapterListSerializer, ChapterDetailSerializer)
from rest_framework.response import Response

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ChapterList(ListAPIView):
    serializer_class = ChapterListSerializer

    def get_queryset(self):
        self.book_lazyloading()
        return Chapter.filter_by_queries(**self.kwargs)

    def book_lazyloading(self):
        book_id = self.kwargs.get("book_id", "")
        book = Book.get_by_queries(id=book_id)
        if book and (not book.chapter_set.all().count()):
            book.lazy_loading()

class ChapterView(APIView):
    def get(self, request, **kwargs):
        chapter = self.get_object(**kwargs)
        serializer = ChapterDetailSerializer(chapter)
        if not chapter:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

    def get_object(self, chapter_id, **kwargs):
        chapter = Chapter.get_by_queries(id=chapter_id)
        if not chapter:
            return None
        else:
            if not chapter.content:
                chapter.lazy_loading()
            return chapter
