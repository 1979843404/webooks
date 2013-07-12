# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from webooks.models import Book
from webooks.spiders.zhangbook import ZhangBookSpider
from webooks.utils.texts import TextSimilarity
from webooks.utils.util import number2chinese

spider = ZhangBookSpider()
text_same = TextSimilarity()

class ZhangBookDiff(object):
    def __init__(self, book_name, src_id):
        self.book_name = book_name
        self.src_id = src_id

    def get_book(self):
        return Book.objects.get(name=self.book_name)

    def get_book_detail(self, name, book_id, chapter, page):
        content = spider.book_detail(name, book_id, chapter, page)
        return content

    def show(self, content, src_content):
        print("爬取后的数据" + "==="*5)
        print(content)
        print("源数据" + "***"*5)
        print(src_content)
        print("相似度%f" %text_same.get_ratio(content, src_content) + "==="*5)

        get_next = raw_input("是否结束: y/n \n".encode("utf-8"))
        if get_next == "y":
            return True
        else:
            return False

    def diff(self):
        book = self.get_book()
        chapters = book.chapters

        for chapter in chapters:
            print("第" + number2chinese(chapter.number) + "章")
            print("共%d页" %chapter.page_set.all().count())
            pages = chapter.page_set.all()
            for page in pages:
                content = page.content
                src_content = self.get_book_detail(self.book_name,
                    self.src_id, chapter.number, page.number)

                get_next = self.show(content, src_content)
                if get_next:
                    break