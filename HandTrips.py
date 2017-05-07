__author__ = 'Nick'

import Hand

class Trips(Hand.Hand):
    def __init__(self, cards):
        super().__init__(cards, cards[0].getHighValue(), 'T')
        self.checkRep()

    def compare(self, t2):
        if self.getPrimaryValue() > t2.getPrimaryValue():
            return True
        elif self.getPrimaryValue() < t2.getPrimaryValue():
            return False
        else:
            return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        for card in self.getCards():
            assert card.getHighValue() == self.getPrimaryValue()



