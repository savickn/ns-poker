__author__ = 'Nick'

import Hand

class TwoPair(Hand.Hand):
    __secondaryValue = None #from the lowest Pair

    def __init__(self, highPair, lowPair):
        super().__init__(highPair.getCards() + lowPair.getCards(), highPair.getPrimaryValue(), 4, 'W')
        self.__secondaryValue = lowPair.getPrimaryValue()
        self.checkRep()

    @staticmethod
    def compare(w1, w2):
        if w1.getPrimaryValue() > w2.getPrimaryValue():
            return w1
        elif w1.getPrimaryValue() < w2.getPrimaryValue():
            return w2
        else:
            if w1.getSecondaryValue() > w2.getSecondaryValue():
                return w1
            elif w1.getSecondaryValue() < w2.getSecondaryValue():
                return w2
            else:
                return None

    def getSecondaryValue(self):
        return self.__secondaryValue

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()

