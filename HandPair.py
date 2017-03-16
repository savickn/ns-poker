__author__ = 'Nick'

import Hand, Deck

class Pair(Hand.Hand):

    def __init__(self, cards, value):
        super().__init__(cards, value, 2, 'P')
        self.checkRep()

    def compare(self, p2):
        if self.getPrimaryValue() > p2.getPrimaryValue():
            return True
        elif self.getPrimaryValue() < p2.getPrimaryValue():
            return False
        else:
            return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        for card in self.getCards():
            assert card.getHighValue() == self.getPrimaryValue()

