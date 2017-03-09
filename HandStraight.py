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

    @staticmethod
    def compare(s1, s2):
        if s1.getPrimaryValue() > s2.getPrimaryValue():
            return s1
        elif s1.getPrimaryValue() < s2.getPrimaryValue():
            return s2
        else:
            return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        assert Helpers.isStraight(self.getCards())