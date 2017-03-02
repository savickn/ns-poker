__author__ = 'Nick'

from PokerCalculator import Hand

class Pair(Hand):
    def __init__(self, pair):
        super(self)
        self.setIdentifier()
        self.checkRep()

    #not fully implemented
    def setIdentifier(self):
        prefix = 'P'
        value = str(self.__value)
        code = str()
        self.__identifier = prefix + value + code

    @staticmethod
    def compare(p1, p2):
        if p1.__value > p2.__value:
            return p1
        elif p1.__value < p2.__value:
            return p2
        else:
            return 'Tied' #maybe return None instead

    def checkRep(self):
        assert len(self.__cards) == 2
        for card in self.__cards:
            assert card.getHighValue() == self.__value