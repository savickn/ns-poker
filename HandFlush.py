__author__ = 'Nick'

import Hand
import Helpers

class Flush(Hand.Hand):
    def __init__(self, cards, value):
        super().__init__(cards, value, 5, 'F')
        self.checkRep()

    @staticmethod
    def compare(f1, f2):
        for c1, c2 in zip(f1, f2):
            if c1.getHighValue() > c2.getHighValue():
                return c1
            elif c2.getHighValue() > c1.getHighValue():
                return c2
            else:
                return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        assert Helpers.isFlush(self.getCards())

