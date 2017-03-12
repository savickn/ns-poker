__author__ = 'Nick'

import Hand

class Trips(Hand.Hand):
    def __init__(self, cards, value):
        super().__init__(cards, value, 3, 'T')
        self.checkRep()

    def compare(self, t2):
        if self.getPrimaryValue() > t2.getPrimaryValue():
            return self
        elif self.getPrimaryValue() < t2.getPrimaryValue():
            return t2
        else:
            return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        for card in self.getCards():
            assert card.getHighValue() == self.getPrimaryValue()



