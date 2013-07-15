# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.views.generic import TemplateView
from webooks.models import Book, Chapter

class BookDetailView(TemplateView):
    template_name = "webooks/detail.html"

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        book = Book.objects.get(**kwargs)
        context["book"] = book
        return context

class BookChapterView(TemplateView):
    template_name = "webooks/chapters.html"

    def get_context_data(self, **kwargs):
        context = super(BookChapterView, self).get_context_data(**kwargs)
        book_id = kwargs['book_id']
        page = int(kwargs.get("page", 1))
        chapters = Chapter.objects.filter(book_id=book_id)[0:10]
        context['chapters'] = chapters
        return context

class ChapterDetailView(TemplateView):
    template_name = "webooks/chapters_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ChapterDetailView, self).get_context_data(**kwargs)
        chapter_id = kwargs['id']
        chapter = Chapter.objects.get(id=chapter_id)
        context['chapter'] = chapter
        return context