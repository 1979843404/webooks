# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from webooks.models import Book, Chapter, Page
from django.contrib import admin
from webooks.forms import ChapterAdminForm

class PageInlineAdmin(admin.StackedInline):
    model = Page
    fields = ("content", )

class BookAdmin(admin.ModelAdmin):
    pass

class ChapterAdmin(admin.ModelAdmin):
    inlines = [PageInlineAdmin,]
    form = ChapterAdminForm

    def full_content(self, obj):
        pages = obj.page_set.all()
        content = ""
        for page in pages:
            content += page.content
            content += "\n"
        return content
    full_content.short_description = u'Full_Content'

class PageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Page, PageAdmin)