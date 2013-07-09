# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from webooks.utils.cache import cache
from webooks.utils.const import USER_STATE
from webooks.models import Book
from webooks.weixin.weixin import WeiXin

WX_INDEX = "index"
WX_SEARCH_BOOKS = "search_books"
WX_BOOK_DETAIL = "book_detail"

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

    def _to_wx_text(self, content):
        wx = WeiXin()
        xml = wx.to_text(from_user_name=self.from_user_name, to_user_name=self.to_user_name, content=content)
        return xml

    def handle(self, content):
        # 根据输入参数返回下一个状态和元数据
        raise NotImplemented

class StateIndex(StateInterface):
    @classmethod
    def initial(cls, from_user_name, to_user_name):
        return cls(from_user_name, to_user_name, meta={
            "content": u"欢迎使用 你的小说 您可以:\n1.搜索\n0.回到首页"
        })

    def handle(self, content):
        if content == "1":
            return WX_SEARCH_BOOKS, {"content": u"进入搜索页, 您可以输入书名进行搜索"}
        else:
            return WX_INDEX, {"content": u"欢迎使用 你的小说 您可以:\n1.搜索\n0.回到首页"}

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
            lines = ["%s:%s" %(book[0], book[1]) for book in books.items()]
            content = "您可以输入数字选择对应的书籍\n" + "\n".join(lines)
        else:
            content = self.meta.get("content", "")
        return self._to_wx_text(content)

    def get_book(self, index):
        return self.meta.get("books", {}).get(index, "")

    def handle(self, content):
        if content == "0":
            return WX_INDEX, {"content": u"欢迎使用 你的小说 您可以:\n1.搜索\n0.回到首页"}

        book = self.get_book(content)
        if book:
            return WX_BOOK_DETAIL, {"content": u"进入%s详情页,功能还在做" % self.meta.get("book", ""), "book": self.get_book(content)}
        else:
            search_books = Book.objects.all().filter(name__icontains=content).values_list("name")
            books = {}
            if not search_books.count():
                return WX_SEARCH_BOOKS, {"content": u"没有结果，请缩小范围", "books": {}}
            else:
                for i, item in enumerate(search_books, start=1):
                    books[str(i)] = item[0]
                return WX_SEARCH_BOOKS, {"content": u"继续搜索", "books": books}

class StateBookDetail(StateInterface):
    def handle(self, content):
        if content == "0":
            return WX_INDEX, {"content": u"回到首页"}
        elif content == "1":
            return WX_BOOK_DETAIL, {"content", u"展示%s章节列表" %self.meta.get("book", "")}
        else:
            return WX_SEARCH_BOOKS, {}

class StateManager(object):
    mapping = {
        WX_INDEX: StateIndex,
        WX_SEARCH_BOOKS: StateSearchBooks,
        WX_BOOK_DETAIL: StateBookDetail
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