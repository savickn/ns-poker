__author__ = 'Nick'

from PokerCalculator import Hand

class Quads(Hand.Hand):
    __prefix = 'Q'

    def __init__(self, quads):
        super().__init__(quads, quads[0].getHighValue(), 4, self.__prefix)
        self.checkRep()

    @staticmethod
    def compare(q1, q2):
        if q1.getValue() > q2.getValue():
            return q1
        elif q1.getValue() < q2.getValue():
            return q2
        else:
            return 'Tied' #maybe return None instead

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        for card in self.getCards():
            assert card.getHighValue() == self.getValue()