__author__ = 'Nick'

from PokerCalculator import PreflopHand

class Range:
    __range = []

    def __init__(self):
        print('range initialized')

    def addHandToRange(self, hand):
        if hand.instanceOf(PreflopHand):
            self.__range.append(hand)

    def removeHandFromRange(self, hand):
        if hand in self.__range:
            self.__range.remove(hand)

