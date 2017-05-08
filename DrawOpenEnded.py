__author__ = 'Nick'

import Draw, Data

class OpenEndedDraw(Draw.Draw):

    def __init__(self, cards, outs):
        super().__init__('F', cards, outs)
        self.checkRep()

    def checkRep(self):
        assert len(self.getCards()) == 4
        assert len(self.getOuts()) == 2

