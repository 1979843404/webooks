# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.http import HttpResponse
from webooks.utils.https import json_response
from weixin import WeiXin

def interface(request):
    if request.method == 'GET':
        echostr = request.GET.get("echostr", "")
        return HttpResponse(echostr)
    else:
        content = request.body
        wx = WeiXin.on_message(content)
        json_data = wx.to_json()
        print(json_data)
        return json_response(json_data)
