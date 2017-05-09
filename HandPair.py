__author__ = 'Nick'

import Hand, Deck

class Pair(Hand.Hand):

    def __init__(self, cards):
        super().__init__(cards, cards[0].getHighValue(), 'P')
        self.checkRep()

    def __str__(self):
        return 'Pair: {cards}'.format(cards=super().__str__())

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

