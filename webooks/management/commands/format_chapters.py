# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.core.management import BaseCommand
from webooks.models import Book
import re

pattern = "chapter=(\d+)"
m = re.compile(pattern)

class Command(BaseCommand):
    def handle(self, *args, **options):
        books = Book.objects.all()
        for book in books:
            self.format(book)

    def format(self, book):
        chapters = book.chapters
        for chapter in chapters:
            url = chapter.src_url
            try:
                real_number = int(m.search(url).group(1))
            except:
                continue
            if chapter.number == real_number:
                continue

            chapter.number = real_number
            chapter.save()
            print("Saving book: %s, chapter: %s" %(unicode(book), unicode(chapter)))