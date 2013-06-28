# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from webooks.models import Book, Chapter, Strategy
from django.contrib import admin
from webooks.forms import ChapterAdminForm


class BookAdmin(admin.ModelAdmin):
    pass

class ChapterAdmin(admin.ModelAdmin):
    form = ChapterAdminForm

class StrategyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Strategy, StrategyAdmin)