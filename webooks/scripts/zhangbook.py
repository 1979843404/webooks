# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
import requests
from xml.etree import cElementTree as ET
from webooks.utils.spiders import SpiderHelper

helper = SpiderHelper()

categories = {
    u"玄幻·奇幻": 1,
    u"武侠·仙侠": 2,
    u"竞技·游戏": 3,
    u"科幻·军事": 4,
    u"灵异·恐怖": 5,
    u"言情·感情": 7,
    u"青春·都市": 8,
    u"耽美·唯美": 9,
    u"动漫·同人": 10,
    u"侦探·推理": 11,
    u"笑话·幽默": 12,
}

def parse_book_list():
    category = u"玄幻·奇幻"
    id = 1

