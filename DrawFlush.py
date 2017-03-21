__author__ = 'Nick'

import Draw, Data

class FlushDraw(Draw.Draw):

    def __init__(self, cards, suit):
        outs = self.calculateOuts(cards, suit)
        super().__init__('F', cards, outs)
        self.__suit = suit
        self.checkRep()

    def calculateOuts(self, cards, suit):
        outs = set(Data.cards[suit]) - set(cards)
        return outs

    def checkRep(self):
        assert len(self.getCards()) == 4


#cards = [Data.king_spades, Data.four_spades, Data.five_spades, Data.nine_spades]

#fd = FlushDraw(cards, cards[0].getSuit())
#for c in fd.getOuts():
#    print(c.toString())