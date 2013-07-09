# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from state import StateManager

class State(object):
    def __init__(self, from_user_name, to_user_name):
        self.to_user_name = to_user_name
        self.from_user_name = from_user_name
        self.state = StateManager.get_user_state(from_user_name, to_user_name)

    def handle(self, content):
        new_state_index, result = self.state.handle(content)
        self.set_state(new_state_index, meta=result)

    def to_xml(self):
        return self.state.to_xml()

    def set_state(self, state="index", meta={}):
        self.state = StateManager.get_state(self.from_user_name, self.to_user_name, state, meta)
        StateManager.set_user_state(self.to_user_name, state, meta)