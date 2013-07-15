# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from webooks.weixin.receiver import WeiXinReceiver

@csrf_exempt
def interface(request):
    if request.method == 'GET':
        echostr = request.GET.get("echostr", "")
        return HttpResponse(echostr)
    else:
        content = request.body
        state = WeiXinReceiver.get_state(content)
        xml_data = state.to_xml()
        return HttpResponse(xml_data)