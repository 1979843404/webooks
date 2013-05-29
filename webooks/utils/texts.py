# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from webooks.utils import const
import Levenshtein

class TextSimilarity(object):
    def get_ratio(self, origin, text):
        return Levenshtein.ratio(origin, text)

    def is_same(self, origin, text):
        ratio = self.get_ratio(origin, text)
        if ratio > const.SIMILARITY_RATIO:
            return True
        else:
            return False
    
