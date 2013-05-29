# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf import settings
import os

# DATABASES
DB_NAME_LENGTH = 128
DB_CONTENT_LENGTH = 256*256*16
DB_NUMBER_DEFAULT = 0

# SPIDERS
SPIDER_BASE_PATH = os.path.join(settings.PROJECT_HOME, 'data')

# CONTENT SIMILARITY
SIMILARITY_RATIO = 0.85