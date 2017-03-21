__author__ = 'Nick'

import Draw, Data

#basically used to represent overcards (e.g. 1 OverpairDraw == 1 overcard, e.g. A9 on KT4)
class OverPairDraw(Draw.Draw):

    def __init__(self, cards, type):
        outs = self.calculateOuts(cards, type)
        super().__init__('P', cards, outs)
        self.checkRep()

    def calculateOuts(self, cards, type):
        outs = set(Data.cards[type]) - set(cards)
        return outs

    def checkRep(self):
        assert len(self.getCards()) == 1

#cards = [Data.king_spades]

#pd = OverPairDraw(cards, cards[0].getType())
#for c in pd.getOuts():
#    print(c.toString())
