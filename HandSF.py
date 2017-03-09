__author__ = 'Nick'

import Hand
import Helpers

class StraightFlush(Hand.Hand):

    def __init__(self, cards, value):
        super().__init__(cards, value, 5, 'Z')
        self.checkRep()

    @staticmethod
    def compare(z1, z2):
        if z1.getPrimaryValue() > z2.getPrimaryValue():
            return z1
        elif z1.getPrimaryValue() < z2.getPrimaryValue():
            return z2
        else:
            return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        assert Helpers.isStraight(self.getCards())
        assert Helpers.isFlush(self.getCards())


