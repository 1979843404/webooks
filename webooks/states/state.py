# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

WX_INDEX = "index"
WX_SEARCH_BOOKS = "search_books"
WX_BOOK_DETAIL = "book_detail"

class StateInterface(object):
    def __init__(self, meta={"content": u"进入首页"}):
        self.meta = meta

    def handle(self, content):
        # 根据输入参数返回下一个状态和元数据
        raise NotImplemented

class StateIndex(StateInterface):
    def handle(self, content):
        if content == "1":
            return WX_SEARCH_BOOKS, {"content": u"进入搜索页"}
        else:
            return WX_INDEX, {"content": "继续"}

class StateSearchBooks(StateInterface):
    def handle(self, content):
        if content == "0":
            return WX_INDEX, {"content": u"回到首页"}
        elif content == "1":
            return WX_BOOK_DETAIL, {"content": u"进入%s详情页" % self.meta.get("book", ""), "book": self.meta.get("book", "")}
        else:
            return WX_SEARCH_BOOKS, {"content": u"继续搜索", "book": content}

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
    def get_state(cls, state="index", meta={}):
        cls_name = cls.mapping.get(state, StateIndex)
        return cls_name(meta)