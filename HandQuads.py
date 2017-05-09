__author__ = 'Nick'

import Hand

class Quads(Hand.Hand):

    def __init__(self, cards):
        super().__init__(cards, cards[0].getHighValue(), 'Q')
        self.checkRep()

    def __str__(self):
        return 'Quads: {cards}'.format(cards=super().__str__())

    def compare(self, q2):
        if self.getPrimaryValue() > q2.getPrimaryValue():
            return True
        elif self.getPrimaryValue() < q2.getPrimaryValue():
            return False
        else:
            return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        for card in self.getCards():
            assert card.getHighValue() == self.getPrimaryValue()