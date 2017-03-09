__author__ = 'Nick'

import Hand, Deck

class Pair(Hand.Hand):

    def __init__(self, cards, value):
        super().__init__(cards, value, 2, 'P')
        self.checkRep()

    @staticmethod
    def compare(p1, p2):
        if p1.getPrimaryValue() > p2.getPrimaryValue():
            return p1
        elif p1.getPrimaryValue() < p2.getPrimaryValue():
            return p2
        else:
            return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        for card in self.getCards():
            assert card.getHighValue() == self.getPrimaryValue()


p1 = [
    Deck.two_hearts,
    Deck.two_spades
]

p2 = [
    Deck.five_clubs,
    Deck.five_spades
]

pair1 = Pair(p1, p1[0].getHighValue())
pair2 = Pair(p2, p2[0].getHighValue())

#winner = Pair.compare(pair1, pair2)
#print(winner.toString())
