__author__ = 'Nick'

import Draw, Data

class BackdoorFlushDraw(Draw.Draw):

    def __init__(self, cards, suit):
        outs = self.calculateOuts(cards, suit)
        super().__init__('F', cards, outs)
        self.__suit = suit
        self.checkRep()

    def __str__(self):
        return '### Backdoor Flush Draw ### \n'\
               '# Suit: {suit} \n' \
               '# Nut: {nut} \n'.format(suit=self.__suit, nut=self.__nut)\
               + super().__str__()

    def calculateOuts(self, cards, suit):
        outs = set(Data.cards[suit]) - set(cards)
        return outs

    def checkRep(self):
        assert len(self.getCards()) == 3