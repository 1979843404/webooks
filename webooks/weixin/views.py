# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.http import HttpResponse

def interface(request):
    if request.method == 'GET':
        echostr = request.GET.get("echostr", "")
    else:
        echostr = ""
    return HttpResponse(echostr)