# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from state import StateManager

class State(object):
    def __init__(self, state="index"):
        self.state = StateManager.get_state(state)

    def handle(self, content):
        new_state_index, result = self.state.handle(content)
        self.set_state(new_state_index, meta=result)

    def show(self):
        self.state.show()

    def set_state(self, state="index", meta={}):
        self.state = StateManager.get_state(state, meta)