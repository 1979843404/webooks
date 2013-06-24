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
    paginate_by = 10
    paginate_by_param = "page"

class ChapterList(ListAPIView):
    serializer_class = ChapterListSerializer
    paginate_by = 10
    paginate_by_param = "page"

    def get_queryset(self):
        return Chapter.filter_by_queries(**self.kwargs)

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
