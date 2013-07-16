# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.views.generic import TemplateView
from webooks.models import Book, Chapter
from webooks.utils.helper import get_url_by_conf
from webooks.utils.paginator import DiggPaginator

class BookDetailView(TemplateView):
    template_name = "webooks/detail.html"

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        book = Book.objects.get(**kwargs)
        context["book"] = book
        context['user_id'] = self.request.GET.get("user_id", "-1")
        return context

class BookChapterView(TemplateView):
    template_name = "webooks/chapters.html"

    def get_context_data(self, **kwargs):
        context = super(BookChapterView, self).get_context_data(**kwargs)
        book_id = kwargs['book_id']
        page = self.request.GET.get("page", 1)
        queryset = Chapter.objects.filter(book_id=book_id)
        paginator = DiggPaginator(queryset, 10, body=5)
        context['page'] = paginator.page(page)
        user_id = self.request.GET.get("user_id", "-1")
        context['base_url'] = get_url_by_conf("book_chapters", args=[book_id], params={
            "user_id": user_id
        })
        context['user_id'] = user_id
        return context

class ChapterDetailView(TemplateView):
    template_name = "webooks/chapters_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ChapterDetailView, self).get_context_data(**kwargs)
        chapter_id = kwargs['id']
        chapter = Chapter.objects.get(id=chapter_id)
        context['chapter'] = chapter
        user_id = self.request.GET.get("user_id", "-1")
        context['before_url'] = get_url_by_conf("book_chapter_detail", args=[chapter.book.id, chapter.before.id], params={
            "user_id": user_id,
        }) if chapter.before else ""
        context['after_url'] = get_url_by_conf("book_chapter_detail", args=[chapter.book.id, chapter.after.id], params={
            "user_id": user_id
        }) if chapter.after else ""
        context['chapter_list_url'] = get_url_by_conf("book_chapters", args=[chapter.book.id], params={
            "user_id": user_id
        })
        context['user_id'] = user_id
        return context