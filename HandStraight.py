__author__ = 'Nick'

import Hand
import Helpers

class Straight(Hand.Hand):

    def __init__(self, cards, value):
        super().__init__(cards, value, 5, 'S')
        try:
            self.checkRep()
        except AssertionError:
            print('This hand is not valid.')

    #used to compare two hands of the same Ranking
    def compare(self, s2):
        if self.getPrimaryValue() > s2.getPrimaryValue():
            return self
        elif self.getPrimaryValue() < s2.getPrimaryValue():
            return s2
        else:
            return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        assert Helpers.isStraight(self.getCards())