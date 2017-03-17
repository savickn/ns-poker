__author__ = 'Nick'

import CalculatorEquity, Range, HandEquity
import Deck

class RangeEquityCalculator:

    def __init__(self, ranges, board=[], iterations=1000):
        self.__ranges = ranges #must be of type Range
        self.__eqCalculators = {

        }
        self.checkRep()

    def calculateEquity(self):
        print()


    ############## UTILITY METHODS ##############

    def checkRep(self):
        assert len(self.__ranges) >= 2
        for r in self.__ranges:
            assert isinstance(r, Range.Range)

d = Deck.Deck([], True)

selected1 = Deck.preflopHands['AKo'] + Deck.preflopHands['AKs']
selected2 = Deck.preflopHands['98o'] + Deck.preflopHands['98s']

r1 = Range.Range(selected1)
r2 = Range.Range(selected2)

req = RangeEquityCalculator([r1, r2])
req.calculateEquity()