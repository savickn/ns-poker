__author__ = 'Nick'

import Action

class Raise(Action.Action):

    def __init__(self, actor, amount, street):
        super().__init__(actor, amount, street)