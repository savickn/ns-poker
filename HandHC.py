__author__ = 'Nick'

import Hand

class HighCards(Hand.Hand):

    def __init__(self, cards):
        super().__init__(cards, max([c.getHighValue() for c in cards]), 'C')
        self.checkRep()

    #used to compare two hands of the same Ranking
    def compare(self, h2):
        for c1, c2 in zip(self.getCards(), h2.getCards()):
            if c1 > c2:
                return True
            elif c2 > c1:
                return False
            else:
                continue
        return None

    def checkRep(self):
        assert len(self.getCards()) == self.getLength()
