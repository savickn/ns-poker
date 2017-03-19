__author__ = 'Nick'

import Hand
import Helpers

class Straight(Hand.Hand):

    def __init__(self, cards, value):
        super().__init__(cards, value, 5, 'S')
        self.checkRep()

    #used to compare two hands of the same Ranking
    def compare(self, s2):
        if self.getPrimaryValue() > s2.getPrimaryValue():
            return True
        elif self.getPrimaryValue() < s2.getPrimaryValue():
            return False
        else:
            return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        assert Helpers.isStraight(self.getCards())