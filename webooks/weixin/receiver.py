# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from weixin import WeiXin
from webooks.states import State

class WeiXinReceiver(object):
    @classmethod
    def get_state(cls, post_data):
        w = WeiXin.on_message(post_data)
        json_data = w.to_json()
        msg_type = json_data.get("MsgType", "")
        handler = getattr(cls, msg_type, cls.text)
        return handler(**json_data)

    @classmethod
    def event(cls, from_user_name, to_user_name, **kwargs):
        state = State.after_subscribe(to_user_name=from_user_name, from_user_name=to_user_name)
        return state

    @classmethod
    def text(cls, from_user_name, to_user_name, **kwargs):
        state = State(to_user_name=from_user_name, from_user_name=to_user_name)
        return state