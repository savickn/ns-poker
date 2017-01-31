__author__ = 'Nick'

from PokerCalculator import PreflopHand, ViewRangeSelection

class Range:
    __range = [] #includes hands that will be played
    #__rangeView = None

    def __init__(self):
        print('range initialized')

    #bind this to button
    def selectRange(self):
        rangeView = ViewRangeSelection.RangeView(self)

    def addHandsToRange(self, hands):
        for hand in hands:
            if hand.instanceOf(PreflopHand):
                print(hand.toString())
                self.__range.append(hand)

    def removeHandsFromRange(self, hands):
        for hand in hands:
            if hand in self.__range:
                print(hand.toString())
                self.__range.remove(hand)



