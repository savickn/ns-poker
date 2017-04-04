__author__ = 'Nick'

import Action

class Check(Action.Action):

    def __init__(self, actor, street):
        super().__init__(actor, 0, street)