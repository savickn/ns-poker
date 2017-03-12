__author__ = 'Nick'

import Hand, Deck

class Pair(Hand.Hand):

    def __init__(self, cards, value):
        super().__init__(cards, value, 2, 'P')
        self.checkRep()

    def compare(self, p2):
        if self.getPrimaryValue() > p2.getPrimaryValue():
            return self
        elif self.getPrimaryValue() < p2.getPrimaryValue():
            return p2
        else:
            return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        for card in self.getCards():
            assert card.getHighValue() == self.getPrimaryValue()


pa1 = [
    Deck.two_hearts,
    Deck.two_spades
]

pa2 = [
    Deck.five_clubs,
    Deck.five_spades
]

pair1 = Pair(pa1, pa1[0].getHighValue())
pair2 = Pair(pa2, pa2[0].getHighValue())

#winner = Pair.compare(pair1, pair2)
#print(winner.toString())
