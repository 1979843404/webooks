# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from weixin import WeiXin
from webooks.states import State
import time

@csrf_exempt
def interface(request):
    if request.method == 'GET':
        echostr = request.GET.get("echostr", "")
        return HttpResponse(echostr)
    else:
        content = request.body
        wx = WeiXin.on_message(content)
        json_data = wx.to_json()
        content = json_data.get("Content", "")
        from_user_name = json_data.get("FromUserName", "")
        to_user_name = json_data.get("ToUserName", "")
        state = State(from_user_name, to_user_name)
        state.handle(content)
        xml_data = state.to_xml()
        return HttpResponse(xml_data)