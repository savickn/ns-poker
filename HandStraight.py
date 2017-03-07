__author__ = 'Nick'

from PokerCalculator import Hand
from PokerCalculator import Helpers

class Straight(Hand):
    __prefix = 'S'

    def __init__(self, straight):
        super().__init__(straight, straight[0].getHighValue(), 5)
        self.setIdentifier()
        self.checkRep()

    def setIdentifier(self):
        value = str(self.__value)
        code = self.generateCode()
        self.__identifier = self.__prefix + value + code

    @staticmethod
    def compare(p1, p2):
        if p1.__value > p2.__value:
            return p1
        elif p1.__value < p2.__value:
            return p2
        else:
            return 'Tied' #maybe return None instead

    def checkRep(self):
        assert len(self.__cards) == 5
        assert Helpers.isStraight(self.__cards)