__author__ = 'Nick'

import Hand

class HighCards(Hand.Hand):

    def __init__(self, cards, value, length):
        super().__init__(cards, value, length, 'C')

        try:
            self.checkRep()
        except AssertionError:
            print('This hand is not valid.')

    #used to compare two hands of the same Ranking
    def compare(self, h2):
        for c1, c2 in self.getCards(), h2.getCards():
            if c1 > c2:
                return self
            elif c2 > c1:
                return h2
            else:
                continue
        return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
