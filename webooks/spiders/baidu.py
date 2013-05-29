# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from spider import Spider

class BaiduSpider(Spider):
    def get_detail_urls(self):
        index_url = "http://top.baidu.com/category?c=10"

