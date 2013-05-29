# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
import hashlib

def md5(input):
    m = hashlib.md5()
    m.update(input)
    return m.hexdigest()

def number2chinese(number):
    number_map = {
        "0": "0",
        "1": "一",
        "2": "二",
        "3": "三",
        "4": "四",
        "5": "五",
        "6": "六",
        "7": "七",
        "8": "八",
        "9": "九"
    }
    digit = ["", "十", "百", "千", "万", "十", "百", "千"]
    text = str(number)
    digits = digit[:len(text)]
    reverse_text = map(lambda x: number_map.get(x, "0"), text[::-1])
    match = zip(reverse_text, digits)
    if match[-1][0] == "0":
        match = match[:-1]
    result = map(lambda x: x[0] + x[1] if x[0] != "0" else '零', match[::-1])
    return "".join(result)