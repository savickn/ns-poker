__author__ = 'Nick'

import Draw, Data

class GutshotDraw(Draw.Draw):

    def __init__(self, cards):
        outs = self.calculateOuts(cards)
        super().__init__('S', cards, outs)
        self.checkRep()

    def calculateOuts(self, cards):
        outs = set(Data.cards[suit]) - set(cards)
        return outs

    def checkRep(self):
        assert len(self.getCards()) == 4
