__author__ = 'Nick'

from PokerCalculator import Hand

class Quads(Hand):
    __quads = None
    __value = None
    __length = 4

    def __init__(self, quads):
        super(self)
        self.__quads = tuple(quads)
        self.__highCard = highCard
        self.__value = quads[0].value

        self.setIdentifier()
        self.checkRep()

    def setIdentifier(self):
        prefix = 'Q'


    def getLength(self):
        return self.__length

    @staticmethod
    def compare(quads1, quads2):
        if quads1.__value > quads2.__value:
            return quads1
        elif quads1.__value < quads2.__value:
            return quads2
        else:
            return 'Tied'

    def checkRep(self):
        assert len(self.__quads) == 4
        #also validate that the hand is actually quads