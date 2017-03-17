__author__ = 'Nick'

import HandPreflop, ViewRangeSelection
import Deck

class Range:
    __rangeView = None

    #add variable to set __Type (e.g. HoldemHand vs. OmahaHand)
    def __init__(self, range=[]):
        self.__range = range

    #bind this to button
    def selectRange(self):
        self.__rangeView = ViewRangeSelection.RangeView(self)

    def addHandsToRange(self, hands):
        for hand in hands:
            if isinstance(hand, HandPreflop.PreflopHand):
                self.__range.append(hand)

    def removeHandsFromRange(self, hands):
        for hand in hands:
            if hand in self.__range:
                self.__range.remove(hand)

    ############ UTILITY METHODS ##############

    def printAsString(self):
        for c in self.__range:
            print(c.toString())

#d = Deck.Deck()
#selectedHands = Deck.preflopHands['AKo'] + Deck.preflopHands['AKs']
#r = Range()
#r.addHandsToRange(selectedHands)
#r.printAsString()





