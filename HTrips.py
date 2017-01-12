__author__ = 'Nick'

from PokerCalculator import Card

#maybe add HandType parent class which implements getLength

class Trips:
    __trips = None
    __value = None
    __length = 3

    def __init__(self, trips):
        self.__trips = tuple(trips)
        self.__value = trips[0].value

        self.checkrep()

    def getLength(self):
        return self.__length

    @staticmethod
    def compare(self, trips1, trips2):
        #compares value of trips
        if trips1.__value > trips2.__value:
            return trips1
        elif trips1.__value < trips2.__value:
            return trips2
        else:
            return 'Tied'

    def checkrep(self):
        assert len(self.__trips) == 3
        #also check that hc1 and hc2 are not null


