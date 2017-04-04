__author__ = 'Nick'

import Action

class PostBB(Action.Action):

    def __init__(self, actor, amount):
        super().__init__(actor, amount, 'PREFLOP')