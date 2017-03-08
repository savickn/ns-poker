__author__ = 'Nick'

import Hand, Deck

class StraightFlush(Hand.Hand):
    __prefix = 'Z'
    __suit = None

    def __init__(self, cards, value, suit):
        super().__init__(cards, value, 5, self.__prefix)
        self.checkRep()

    @staticmethod
    def compare(z1, z2):
        if z1.getValue() > z2.getValue():
            return z1
        elif z1.getValue() < z2.getValue():
            return z2
        else:
            return None

    def getPrefix(self):
        return self.__prefix

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        for card in self.getCards():
            assert card.getSuit() == self.__suit


