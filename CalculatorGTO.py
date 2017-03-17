__author__ = 'Nick'

import Deck, Board


#used to rank hands within a range to determine which X% should be called vs. a pot-size bet/etc
class GtoSolver:
    __deck = None
    __board = None
    __hands = None
    __iterations = None

    def __init__(self, iterations):
        self.__deck = Deck.Deck()
        self.__iterations = iterations

    ######## GETTERS and SETTERS ########

    def setIterations(self, iterations):
        self.__iterations = iterations


    def run_iteration(self):
        self.__deck.shuffleDeck()
        self.generateFlop()
        self.generateTurn()
        self.generateRiver()



    def get_preflop_equity(self, hero, villain):
        #1 v 1 hands
        print()

    def get_postflop_equity(self, hero, villain, board):
        print()

    def get_equity_range(hero_array, villain_array):
        print()


    ######### Community Card Actions ############

    def burnCard(self):
        self.__deck.getTopCard()

    def generateFlop(self):
        self.burnCard()
        card1 = self.__deck.getTopCard()
        card2 = self.__deck.getTopCard()
        card3 = self.__deck.getTopCard()
        self.__board = Board.Board(card1, card2, card3)

    def generateTurn(self):
        self.burnCard()
        card4 = self.__deck.getTopCard()
        self.__board.setTurn(card4)

    def generateRiver(self):
        self.burnCard()
        card5 = self.__deck.getTopCard()
        self.__board.setRiver(card5)




#def get_equity(self, hero, villain, board=[]):
#    assert len(board) in range(3, 6)
#    raw_equity = 0
#    avg_equity = 0
#    for x in range(1, self.__iterations + 1):
#        raw_equity += self.run_iteration()
#    avg_equity = raw_equity/self.__iterations
#    return avg_equity
