# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from webooks.utils import const
from webooks.utils.util import md5
import requests
import os

class Spider(object):
    def get_detail_urls(self):
        raise NotImplemented

    def run(self):
        for url in self.get_detail_urls():
            content = self.crawler(url)
            self.save(url, content)

