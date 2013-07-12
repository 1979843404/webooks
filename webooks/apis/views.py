# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from webooks.models import Book, Chapter
from webooks.apis.serializers.books import (BookSerializer, BookDetailSerializer,
                                            ChapterListSerializer, ChapterDetailSerializer)
from rest_framework.response import Response

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(APIView):
    def get_object(self, book_id, **kwargs):
        book = Book.get_by_queries(id=book_id)
        if not book:
            return None
        return book

    def get(self, request, **kwargs):
        book = self.get_object(**kwargs)
        serializer = BookDetailSerializer(book)
        if not book:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

class ChapterList(ListAPIView):
    serializer_class = ChapterListSerializer

    def get_queryset(self):
        """最好的写法是
        Chapter.filter_by_queries(**self.kwargs)
        为了lazy loading，改下
        """
        book = Book.get_by_unique(id=self.kwargs.get("book_id", ""))
        return book.chapters

class ChapterView(APIView):
    def get(self, request, **kwargs):
        chapter = self.get_object(**kwargs)
        serializer = ChapterDetailSerializer(chapter)
        if not chapter:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

    def get_object(self, chapter_id, **kwargs):
        chapter = Chapter.get_by_queries(id=chapter_id)
        return chapter
