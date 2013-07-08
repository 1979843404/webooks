# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from state import StateManager

class State(object):
    def __init__(self, user_key):
        self.user_key = user_key
        self.state = StateManager.get_user_state(user_key)

    def handle(self, content):
        new_state_index, result = self.state.handle(content)
        self.set_state(new_state_index, meta=result)

    def show(self):
        return self.state.show()

    def set_state(self, state="index", meta={}):
        self.state = StateManager.get_state(state, meta)
        StateManager.set_user_state(self.user_key, state, meta)