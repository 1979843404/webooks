# -*- coding: utf-8 -*-
# __author__ = chenchiyuan
from __future__ import division, unicode_literals, print_function
from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse

def pil_image(request):
    size = (500, 500)
    im = Image.new("RGB", size)

    draw = ImageDraw.Draw(im)
    red = (255, 0, 0)
    text_pos = (200,200)
    text = request.GET.get("content", "test")
    font = ImageFont.load_default()

    draw.text(text_pos, text.encode("utf-8"), fill=red, font=font)
    response = HttpResponse(mimetype="image/png")
    im.save(response, 'png')

    return response