__author__ = 'Nick'

import Draw, Data

class FlushDraw(Draw.Draw):

    def __init__(self, cards, suit):
        outs = self.calcOuts(cards, suit)
        super().__init__('F', cards, outs)
        self.__suit = suit

        # will this hand make the nut-flush/straight, must be Boolean,
        # probably not needed cuz can find the resulting BestHand in the ordered list of BestHands
        self.__nut = self.calcNut()

        self.checkRep()

    def __str__(self):
        return '### Flush Draw ### \n'\
               '# Suit: {suit} \n' \
               '# Nut: {nut} \n'.format(suit=self.__suit, nut=self.__nut)\
               + super().__str__()

    def calcOuts(self, cards, suit):
        outs = set(Data.cards[suit]) - set(cards)
        return outs

    def calcNut(self):
        self.__nut = False
        for c in self.getCards():
            if c.getHighValue() == 14:
                self.__nut = True

    def checkRep(self):
        assert len(self.getCards()) == 4


#cards = [Data.king_spades, Data.four_spades, Data.five_spades, Data.nine_spades]

#fd = FlushDraw(cards, cards[0].getSuit())
#for c in fd.getOuts():
#    print(c.toString())