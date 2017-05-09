__author__ = 'Nick'

import Hand
from Helpers import FlushHelpers

class StraightFlush(Hand.Hand):

    def __init__(self, cards, value):
        super().__init__(cards, value, 'Z')
        self.checkRep()

    def __str__(self):
        return 'Straight Flush: {cards}'.format(cards=super().__str__())

    def compare(self, z2):
        if self.getPrimaryValue() > z2.getPrimaryValue():
            return True
        elif self.getPrimaryValue() < z2.getPrimaryValue():
            return False
        else:
            return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        #assert Helpers.isStraight(self.getCards())
        assert FlushHelpers.isFlush(self.getCards())


