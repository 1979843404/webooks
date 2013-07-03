# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.http import HttpResponse

def books(request):
    data = request.REQUEST
    return HttpResponse(data)

def chapters(request):
    data = request.REQUEST
    return HttpResponse(data)

def chapter(request):
    data = request.REQUEST
    return HttpResponse(data)

