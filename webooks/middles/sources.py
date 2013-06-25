# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from interfaces import SourceInterface
from webooks.spiders import SpiderFactory
from webooks.models.services import BookService, ChapterService

class SourceZhangBook(SourceInterface):
    spider = SpiderFactory.get_spider("ZhangBookSpider")

    def get_all_books(self, *args, **kwargs):
        books = self.spider.get_all_books(*args, **kwargs)
        self.save_books(books)

    def get_chapters(self, book, *args, **kwargs):
        chapters = self.spider.get_chapters(book.name, book_id=book.src_id, start=1)
        for chapter in chapters:
            chapter['book_id'] = book.id
            print("Saving >>>>>")
            print(chapter['title'])
            print(chapter['number'])
            item = ChapterService.get_or_create(queries=chapter, **chapter)
            print("<<<<< Done")

    def get_book_detail(self, book, *args, **kwargs):
        book_id = book.src_id
        is_over = book.is_over
        content = self.spider.get_book_detail(book_id, cache=is_over, **kwargs)
        for key, value in content.items():
            setattr(book, key, value)
        book.save()

    def get_chapter_content(self, chapter, *args, **kwargs):
        content = self.spider.get_chapter_content(chapter.book.src_id, chapter.number)
        if not content:
            return ""
        else:
            chapter.content = content
            chapter.save()

    def save_books(self, items):
        books = []
        for name, kwargs in items.items():
            books.append({
                "queries": {
                    "name": name,
                    "src_name": "zhangbook",
                },
                "kwargs": kwargs
            })
        for book in books:
            BookService.get_or_create(book["queries"], **book["kwargs"])

