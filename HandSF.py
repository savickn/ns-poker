__author__ = 'Nick'

import Hand
import Helpers

class StraightFlush(Hand.Hand):

    def __init__(self, cards, value):
        super().__init__(cards, value, 5, 'Z')
        self.checkRep()

    def compare(self, z2):
        if self.getPrimaryValue() > z2.getPrimaryValue():
            return self
        elif self.getPrimaryValue() < z2.getPrimaryValue():
            return z2
        else:
            return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        assert Helpers.isStraight(self.getCards())
        assert Helpers.isFlush(self.getCards())


