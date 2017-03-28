__author__ = 'Nick'

import Action

class Call(Action.Action):

    def __init__(self, actor, amount):
        super().__init__(actor, amount)