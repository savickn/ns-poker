__author__ = 'Nick'

import Hand

class TwoPair(Hand.Hand):
    __secondaryValue = None #from the lowest Pair

    def __init__(self, highPair, lowPair):
        super().__init__(highPair.getCards() + lowPair.getCards(), highPair.getPrimaryValue(), 4, 'W')
        self.__secondaryValue = lowPair.getPrimaryValue()
        self.checkRep()

    def compare(self, w2):
        if self.getPrimaryValue() > w2.getPrimaryValue():
            return True
        elif self.getPrimaryValue() < w2.getPrimaryValue():
            return False
        else:
            if self.getSecondaryValue() > w2.getSecondaryValue():
                return True
            elif self.getSecondaryValue() < w2.getSecondaryValue():
                return False
            else:
                return None

    def getSecondaryValue(self):
        return self.__secondaryValue

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()

