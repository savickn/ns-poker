__author__ = 'Nick'

import Hand, Deck

class Pair(Hand.Hand):

    def __init__(self, cards, value):
        super().__init__(cards, value, 2, 'P')
        self.checkRep()

    @staticmethod
    def compare(p1, p2):
        if p1.getValue() > p2.getValue():
            return p1
        elif p1.getValue() < p2.getValue():
            return p2
        else:
            return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        for card in self.getCards():
            assert card.getHighValue() == self.getValue()

