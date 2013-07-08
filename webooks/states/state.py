# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from webooks.utils.cache import cache
from webooks.utils.const import USER_STATE

WX_INDEX = "index"
WX_SEARCH_BOOKS = "search_books"
WX_BOOK_DETAIL = "book_detail"

class StateInterface(object):
    def __init__(self, meta={}):
        self.meta = meta

    @classmethod
    def initial(cls):
        return cls(meta={})

    def show(self):
        print(self.meta.get("content", ""))

    def handle(self, content):
        # 根据输入参数返回下一个状态和元数据
        raise NotImplemented

class StateIndex(StateInterface):
    @classmethod
    def initial(cls):
        return cls(meta={
            "content": u"首页\n1.搜索\n0.回到首页"
        })

    def handle(self, content):
        if content == "1":
            return WX_SEARCH_BOOKS, {"content": u"进入搜索页"}
        else:
            return WX_INDEX, {"content": "继续"}

class StateSearchBooks(StateInterface):
    @classmethod
    def initial(cls):
        return cls(meta={
            "content": u"进入搜索页",
            "books": {}
        })

    def show(self):
        books = self.meta.get("books", {})
        if books:
            lines = ["%s:%s" %(book[0], book[1]) for book in books.items()]
            print("\n".join(lines))
        else:
            print(self.meta.get("content", ""))

    def get_book(self, index):
        return self.meta["books"].get(index, "")

    def handle(self, content):
        if content == "0":
            return WX_INDEX, {"content": u"回到首页"}
        elif content == "1":
            return WX_BOOK_DETAIL, {"content": u"进入%s详情页" % self.meta.get("book", ""), "book": self.get_book(content)}
        else:
            return WX_SEARCH_BOOKS, {"content": u"继续搜索", "books": {"1": content}}

class StateBookDetail(StateInterface):
    def handle(self, content):
        if content == "0":
            return WX_INDEX, {"content": u"回到首页"}
        elif content == "1":
            return WX_SEARCH_BOOKS, {"content", u"进入搜索页"}
        else:
            return WX_BOOK_DETAIL, {"content", u"展示%s章节列表" %self.meta.get("book", "")}

class StateManager(object):
    mapping = {
        WX_INDEX: StateIndex,
        WX_SEARCH_BOOKS: StateSearchBooks,
        WX_BOOK_DETAIL: StateBookDetail
    }

    @classmethod
    def get_user_state(cls, user_key):
        info = cache.get(USER_STATE(user_key))
        if not info:
            return cls.get_state()
        else:
            return cls.get_state(**info)

    @classmethod
    def set_user_state(cls, user_key, state="index", meta={}):
        info = {
            "state": state,
            "meta": meta,
        }
        return cache.set(USER_STATE(user_key), info)

    @classmethod
    def clear_user_state(cls, user_key):
        return cache.delete(USER_STATE(user_key))

    @classmethod
    def get_state(cls, state="index", meta={}):
        cls_name = cls.mapping.get(state, StateIndex)
        if not meta:
            return cls_name.initial()
        else:
            return cls_name(meta)