__author__ = 'Nick'

import Draw

class DrawFlush(Draw.Draw):

    def __init__(self, cards, suit):
        super().__init__(cards)
        self.__suit = suit
        self.checkRep()

    def checkRep(self):
        print()

