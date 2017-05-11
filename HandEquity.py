__author__ = 'Nick'

#holds equity information for a single hand
class Equity:
    def __init__(self, hand):
        self.__hand = hand #must be type PreflopHand
        self.__count = 0
        self.__equity = 0

    def __str__(self):
        return '{hand}-{equity}'.format(hand=self.__hand.__str__(), equity=self.getEquity())

    def getHand(self):
        return self.__hand

    def getEquity(self):
        return self.__equity/self.__count if self.__count > 0 else 0

    def updateEquity(self, equity):
        self.__equity += equity
        self.__count += 1