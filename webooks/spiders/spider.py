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

    def get_path(self, url):
        path = os.path.join(const.SPIDER_BASE_PATH, self.__class__.__name__)
        if not os.path.exists(path):
            os.makedirs(path)
        return os.path.join(path, md5(url))

    def run(self):
        for url in self.get_detail_urls():
            content = self.crawler(url)
            self.save(url, content)

    def crawler(self, url, *args, **kwargs):
        res = requests.get(url)
        return res.content

    def save(self, url, content):
        path = self.get_path(url)
        file = open(path, "w")
        file.write(content)
        file.close()