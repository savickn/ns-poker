__author__ = 'Nick'

import Hand

class FullHouse(Hand.Hand):
    __secondaryValue = None #from the Pair

    def __init__(self, trips, pair):
        super().__init__(trips.getCards() + pair.getCards(), trips.getPrimaryValue(), 5, 'B')
        self.__secondaryValue = pair.getPrimaryValue()
        self.checkRep()

    def compare(self, z2):
        if self.getPrimaryValue() > z2.getPrimaryValue():
            return self
        elif self.getPrimaryValue() < z2.getPrimaryValue():
            return z2
        else:
            if self.getSecondaryValue() > z2.getSecondaryValue():
                return self
            elif self.getSecondaryValue() < z2.getSecondaryValue():
                return z2
            else:
                return None

    def getSecondaryValue(self):
        return self.__secondaryValue

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()


