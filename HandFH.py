__author__ = 'Nick'

import Hand

class FullHouse(Hand.Hand):
    __secondaryValue = None #from the Pair

    def __init__(self, trips, pair):
        super().__init__(trips.getCards() + pair.getCards(), trips.getPrimaryValue(), 5, 'B')
        self.__secondaryValue = pair.getPrimaryValue()
        self.checkRep()

    @staticmethod
    def compare(z1, z2):
        if z1.getPrimaryValue() > z2.getPrimaryValue():
            return z1
        elif z1.getPrimaryValue() < z2.getPrimaryValue():
            return z2
        else:
            if z1.getSecondaryValue() > z2.getSecondaryValue():
                return z1
            elif z1.getSecondaryValue() < z2.getSecondaryValue():
                return z2
            else:
                return None

    def getSecondaryValue(self):
        return self.__secondaryValue

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()


