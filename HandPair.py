__author__ = 'Nick'

from PokerCalculator import Hand, Deck

class Pair(Hand.Hand):
    __prefix = 'P'

    def __init__(self, pair):
        super().__init__(pair, pair[0].getHighValue(), 2, self.__prefix)
        self.checkRep()

    @staticmethod
    def compare(p1, p2):
        if p1.getValue() > p2.getValue():
            return p1
        elif p1.getValue() < p2.getValue():
            return p2
        else:
            return 'Tied' #maybe return None instead

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        for card in self.getCards():
            assert card.getHighValue() == self.getValue()


pair = [
    Deck.ace_hearts,
    Deck.ace_spades
]
p = Pair(pair)

#print('#############')
#print(p.getValue())
#print(p.getLength())
#print(p.getCards())
#print(p.getIdentifier())