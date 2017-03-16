__author__ = 'Nick'

import Hand
import Helpers

class Flush(Hand.Hand):
    def __init__(self, cards, value):
        super().__init__(cards, value, 5, 'F')
        self.checkRep()

    def compare(self, f2):
        for c1, c2 in self, f2:
            if c1 > c2:
                return True
            elif c2 > c1:
                return False
            else:
                continue
        return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
        assert Helpers.isFlush(self.getCards())

    def toString(self):
        string = 'Flush: '
        for card in self.getCards():
            string += '{card}, '.format(card=card.toString())
