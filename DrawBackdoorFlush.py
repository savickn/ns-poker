__author__ = 'Nick'

import Draw, Data

class BackdoorFlushDraw(Draw.Draw):

    def __init__(self, cards, suit):
        outs = self.calculateOuts(cards, suit)
        super().__init__('F', cards, outs)
        self.__suit = suit
        self.checkRep()

    def calculateOuts(self, cards, suit):
        outs = set(Data.cards[suit]) - set(cards)
        return outs

    def checkRep(self):
        assert len(self.getCards()) == 3