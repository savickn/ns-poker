__author__ = 'Nick'

from PokerCalculator import Hand

class Trips(Hand.Hand):
    __prefix = 'T'

    def __init__(self, trips):
        super().__init__(trips, trips[0].getHighValue(), 3, self.__prefix)
        self.checkRep()

    @staticmethod
    def compare(t1, t2):
        if t1.getValue() > t2.getValue():
            return t1
        elif t1.getValue() < t2.getValue():
            return t2
        else:
            return 'Tied' #maybe return None instead

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        for card in self.getCards():
            assert card.getHighValue() == self.getValue()



