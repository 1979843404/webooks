# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from webooks.utils.cache import cache
from webooks.utils.const import USER_STATE
from webooks.models import Book
from webooks.weixin.weixin import WeiXin
from collections import OrderedDict

WX_INDEX = "index"
WX_SEARCH_BOOKS = "search_books"
WX_BOOK_DETAIL = "book_detail"
WX_SEARCH_AUTHORS ="search_authors"

class StateInterface(object):
    def __init__(self, from_user_name, to_user_name, meta={}):
        self.from_user_name = from_user_name
        self.to_user_name = to_user_name
        self.meta = meta

    @classmethod
    def initial(cls, from_user_name, to_user_name):
        return cls(from_user_name, to_user_name, meta={})

    def to_xml(self):
        content = self.meta.get("content", "")
        return self._to_wx_text(content)

    def _to_wx_text(self, content=""):
        wx = WeiXin()
        xml = wx.to_text(from_user_name=self.from_user_name, to_user_name=self.to_user_name, content=content)
        return xml

    def _to_full_text(self, articles):
        wx = WeiXin()
        xml = wx.to_pic_text(from_user_name=self.from_user_name, to_user_name=self.to_user_name,
            articles=articles)
        return xml

    def handle(self, content):
        # 根据输入参数返回下一个状态和元数据
        raise NotImplemented

class StateIndex(StateInterface):
    @classmethod
    def initial(cls, from_user_name, to_user_name):
        return cls(from_user_name, to_user_name, meta={
            "content": u"欢迎使用 你的小说 您可以:\n1.搜书名\n2.搜作者\n0.回到首页"
        })

    def handle(self, content):
        if content == "1":
            return WX_SEARCH_BOOKS, {}
        elif content == "2":
            return WX_SEARCH_AUTHORS, {}
        elif content == "3":
            return WX_INDEX, {}
        else:
            return WX_INDEX, {}

class StateSearchAuthors(StateInterface):
    @classmethod
    def initial(cls, from_user_name, to_user_name):
        return cls(from_user_name, to_user_name, meta={
            "content": u"进入搜索页, 您可以输入作者名进行搜索",
            "books": {}
        })

    def get_book(self, index):
        return self.meta.get("books", {}).get(index, {})

    def to_xml(self):
        books = self.meta.get("books", {})
        if books:
            lines = ["%s:%s 作者:%s" %(index, book.get("name", ""), book.get("author", "")) for index, book in books.items()]
            content = "您可以输入数字选择对应的书籍\n" + "\n".join(lines)
            content += "\n0:回到首页"
        else:
            content = self.meta.get("content", "")
        return self._to_wx_text(content)

    def handle(self, content):
        if content == "0":
            return WX_INDEX, {}

        book = self.get_book(content)
        if book:
            return WX_BOOK_DETAIL, {
                "content": u"进入%s详情页" % self.meta.get("book", ""),
                "book": book
            }
        else:
            search_books = Book.objects.all().filter(author=content)
            books = OrderedDict()
            if not search_books.count():
                return WX_SEARCH_BOOKS, {"content": u"没有结果，请缩小范围", "books": {}}
            else:
                for i, item in enumerate(search_books, start=1):
                    books[str(i)] = {
                        "id": item.id,
                        "name": item.name,
                        "author": item.author
                    }
                return WX_SEARCH_BOOKS, {"content": u"继续搜索", "books": books}

class StateSearchBooks(StateInterface):
    @classmethod
    def initial(cls, from_user_name, to_user_name):
        return cls(from_user_name, to_user_name, meta={
            "content": u"进入搜索页, 您可以输入书名进行搜索",
            "books": {}
        })

    def to_xml(self):
        books = self.meta.get("books", {})
        if books:
            lines = ["%s:%s 作者:%s" %(index, book.get("name", ""), book.get("author", "")) for index, book in books.items()]
            content = "您可以输入数字选择对应的书籍\n" + "\n".join(lines)
            content += "\n0:回到首页"
        else:
            content = self.meta.get("content", "")
        return self._to_wx_text(content)

    def get_book(self, index):
        return self.meta.get("books", {}).get(index, {})

    def handle(self, content):
        if content == "0":
            return WX_INDEX, {}

        book = self.get_book(content)
        if book:
            return WX_BOOK_DETAIL, {
                "content": u"进入%s详情页" % self.meta.get("book", ""),
                "book": book
            }
        else:
            search_books = Book.objects.all().filter(name__icontains=content)
            books = OrderedDict()
            if not search_books.count():
                return WX_SEARCH_BOOKS, {"content": u"没有结果，请缩小范围", "books": {}}
            else:
                for i, item in enumerate(search_books, start=1):
                    books[str(i)] = {
                        "id": item.id,
                        "name": item.name,
                        "author": item.author
                    }
                return WX_SEARCH_BOOKS, {"content": u"继续搜索", "books": books}

class StateBookDetail(StateInterface):
    def to_xml(self):
        book = self.meta.get("book", "")
        if book:
            item = Book.objects.get(id=book["id"])
            articles = [
                {
                    "title": u"%s" % item.name,
                    "description": u"%s" %item.description,
                    "picurl": "http://cayman.b0.upaiyun.com/71509cef7a4940aea89fa6d512be8715.jpeg!medium",
                    "url": item.absolute_url,
                }
            ]
            return self._to_full_text(articles)
        else:
            return self._to_wx_text(self.meta.get("content", ""))

    def handle(self, content):
        if content == "0":
            return WX_INDEX, {"content": u"回到首页"}
        elif content == "1":
            return WX_BOOK_DETAIL, {
                "content": u"展示%s章节列表" %self.meta.get("book", {}).get("name", ""), "book": self.meta.get("book", "")
            }
        else:
            return WX_SEARCH_BOOKS, {}

class StateManager(object):
    mapping = {
        WX_INDEX: StateIndex,
        WX_SEARCH_BOOKS: StateSearchBooks,
        WX_BOOK_DETAIL: StateBookDetail,
        WX_SEARCH_AUTHORS: StateSearchAuthors
    }

    @classmethod
    def get_user_state(cls, from_user_name, to_user_name):
        info = cache.get(USER_STATE(to_user_name))
        if not info:
            return cls.get_state(from_user_name, to_user_name)
        else:
            return cls.get_state(from_user_name, to_user_name, **info)

    @classmethod
    def set_user_state(cls, to_user_name, state="index", meta={}):
        info = {
            "state": state,
            "meta": meta,
        }
        return cache.set(USER_STATE(to_user_name), info)

    @classmethod
    def clear_user_state(cls, to_user_name):
        return cache.delete(USER_STATE(to_user_name))

    @classmethod
    def get_state(cls, from_user_name, to_user_name, state="index", meta={}):
        cls_name = cls.mapping.get(state, StateIndex)
        if not meta:
            return cls_name.initial(from_user_name, to_user_name)
        else:
            return cls_name(from_user_name, to_user_name, meta)