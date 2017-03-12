__author__ = 'Nick'

import Hand

class Quads(Hand.Hand):

    def __init__(self, cards, value):
        super().__init__(cards, value, 4, 'Q')
        self.checkRep()

    def compare(self, q2):
        if self.getPrimaryValue() > q2.getPrimaryValue():
            return self
        elif self.getPrimaryValue() < q2.getPrimaryValue():
            return q2
        else:
            return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        for card in self.getCards():
            assert card.getHighValue() == self.getPrimaryValue()