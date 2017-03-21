__author__ = 'Nick'

import Draw, Data

class OpenEndedDraw(Draw.Draw):

    def __init__(self, cards):
        outs = self.calculateOuts(cards)
        super().__init__('F', cards, outs)
        self.checkRep()

    def calculateOuts(self, cards):
        outs = set(Data.cards[0]) - set(cards)
        return outs

    def checkRep(self):
        assert len(self.getCards()) == 4
