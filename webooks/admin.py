# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from webooks.models import Book, Chapter, Strategy
from django.contrib import admin
from webooks.forms import ChapterAdminForm


class BookAdmin(admin.ModelAdmin):
    list_filter = ("is_over", )
    search_fields = ("name", )
    list_display = ['name', "author", "description", "score", "src_url", "chapter_count"]

    def chapter_count(self, obj):
        return obj.chapter_set.count()
    chapter_count.short_description = u"章节数"

class ChapterAdmin(admin.ModelAdmin):
    form = ChapterAdminForm
    search_fields = ("book__name", )
    ordering = ["number"]
    list_display = ["title", "book", "number", "src_url"]

    ordering = ['book', "number"]

class StrategyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Strategy, StrategyAdmin)