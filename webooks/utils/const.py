# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf import settings
import os

# DATABASES
DB_NAME_LENGTH = 128
DB_CONTENT_LENGTH = 256*256*12
DB_DESCRIPTION_LENGTH = 256*24
DB_NUMBER_DEFAULT = 0

# URL CONFIG
URL_BOOK_ID = "(?P<book_id>[0-9]+)"
URL_CHAPTER_ID = "(?P<chapter_id>[0-9]+)"

# SPIDERS
SPIDER_BASE_PATH = "/Volumes/Macintosh HD/Users/shadow/data" #os.path.join(settings.PROJECT_HOME, 'data')
SPIDER_HASH = 200
SPIDER_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.7a) Gecko/20050614 Firefox/0.9.0+"
}

# CONTENT SIMILARITY
SIMILARITY_RATIO = 0.85