__author__ = 'Nick'


class Board:
    __flop1 = None
    __flop2 = None
    __flop3 = None
    __turn = None
    __river = None

    def __init__(self, card1, card2, card3, card4=None, card5=None):
        self.__flop1 = card1
        self.__flop2 = card2
        self.__flop3 = card3
        self.__turn = card4
        self.__river = card5

    def getCards(self):
        board = [self.__flop1, self.__flop2, self.__flop3]
        if self.__turn is not None:
            board.append(self.__turn)
            if self.__river is not None:
                board.append(self.__river)
        return board

    def setTurn(self, turn):
        self.__turn = turn
        assert len(self.getCards()) is 4

    def setRiver(self, river):
        self.__river = river
        assert len(self.getCards()) is 5

    ############# UTILITY METHODS ##################

    def toString(self):
        string = ''
        for card in self.getCards():
            string += '{card}, '.format(card = card.toString())
        #add method to remove trailing , from string output
        return string

    def printAsString(self):
        print(self.toString())

    def draw(self):
        for card in self.getCards():
            card.draw()

    def checkRep(self):
        assert self.getCards() in range(3,6)

