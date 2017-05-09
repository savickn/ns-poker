__author__ = 'Nick'

import Hand
from Helpers import FlushHelpers

class Flush(Hand.Hand):
    def __init__(self, cards):
        super().__init__(cards, max([c.getHighValue() for c in cards]), 'F')
        self.checkRep()

    def __str__(self):
        return 'Flush: {cards}'.format(cards=super().__str__())

    def compare(self, f2):
        for c1, c2 in self, f2:
            if c1 > c2:
                return True
            elif c2 > c1:
                return False
            else:
                continue
        return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        assert FlushHelpers.isFlush(self.getCards())

    def toString(self):
        string = 'Flush: '
        for card in self.getCards():
            string += '{card}, '.format(card=card.toString())
