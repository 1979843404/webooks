# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from state import StateManager
from state import WX_AFTER_SUBSCRIBE

class State(object):
    def __init__(self, from_user_name, to_user_name, **kwargs):
        self.to_user_name = to_user_name
        self.from_user_name = from_user_name
        self.state = StateManager.get_user_state(from_user_name, to_user_name)

    @classmethod
    def after_subscribe(cls, from_user_name, to_user_name, **kwargs):
        item = cls(from_user_name, to_user_name, **kwargs)
        item.set_state(state=WX_AFTER_SUBSCRIBE)
        return item

    def handle(self, content):
        new_state_index, result = self.state.handle(content)
        self.set_state(new_state_index, meta=result)

    def to_xml(self):
        return self.state.to_xml()

    def set_state(self, state="index", meta={}):
        self.state = StateManager.get_state(self.from_user_name, self.to_user_name, state, meta)
        StateManager.set_user_state(self.to_user_name, state, meta)