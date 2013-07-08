# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from weixin import WeiXin
from webooks.models import Book
import time

@csrf_exempt
def interface(request):
    print(request)
    if request.method == 'GET':
        echostr = request.GET.get("echostr", "")
        return HttpResponse(echostr)
    else:
        content = request.body
        wx = WeiXin.on_message(content)
        json_data = wx.to_json()
        content = json_data.get("Content", "")
        books = Book.objects.all().filter(name__icontains=content).values_list('name')
        book_contents = [book[0] for book in books]
        book_content = "\n".join(book_contents)
        to_user_name = json_data.get("FromUserName", "")
        from_user_name = json_data.get("ToUserName", "")
        create_time = time.time()
        msg_type = "text"
        content = book_content
        func_flag = 0
        xml_data = wx.to_xml(to_user_name=to_user_name, from_user_name=from_user_name, create_time=create_time,
            msg_type=msg_type, content=content, func_flag=func_flag)

        return HttpResponse(xml_data)