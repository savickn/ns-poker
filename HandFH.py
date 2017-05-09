__author__ = 'Nick'

import Hand

class FullHouse(Hand.Hand):

    def __init__(self, trips, pair):
        super().__init__(trips.getCards() + pair.getCards(), trips.getPrimaryValue(), 'B')
        self.__secondaryValue = pair.getPrimaryValue() #from the Pair
        self.checkRep()

    def __str__(self):
        return 'Full House: {cards}'.format(cards=super().__str__())

    def compare(self, z2):
        if self.getPrimaryValue() > z2.getPrimaryValue():
            return True
        elif self.getPrimaryValue() < z2.getPrimaryValue():
            return False
        else:
            if self.getSecondaryValue() > z2.getSecondaryValue():
                return True
            elif self.getSecondaryValue() < z2.getSecondaryValue():
                return False
            else:
                return None

    def getSecondaryValue(self):
        return self.__secondaryValue

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()


