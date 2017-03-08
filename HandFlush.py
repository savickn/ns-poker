__author__ = 'Nick'

import Hand, Deck
import Helpers

class Flush(Hand.Hand):
    __prefix = 'F'
    __suit = None

    def __init__(self, cards, value, suit):
        super().__init__(cards, value, 5, self.__prefix)
        self.__suit = suit
        self.checkRep()

    @staticmethod
    def compare(f1, f2):
        for c1, c2 in zip(f1, f2):
            if c1.getHighValue() > c2.getHighValue():
                return c1
            elif c2.getHighValue() > c1.getHighValue():
                return c2
            else:
                return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        for card in self.getCards():
            assert card.getSuit() == self.__suit



#print('#############')
#print(p.getValue())
#print(p.getLength())
#print(p.getCards())
#print(p.getIdentifier())