__author__ = 'Nick'

from PokerCalculator import HandPreflop, Board, Deck, HandAnalyzer

board1 = []
hand1 = []
hand2 = []

class HandData:
    __hand = None
    __iterations = 0
    __rawEquity = 0
    __avgEquity = 0

    def __init__(self, hand):
        self.__hand = hand

    def getHand(self):
        return self.__hand

    def incrementIterations(self):
        self.__iterations += 1

    def addRawEquity(self, equity):
        self.__rawEquity += equity

    def calcEquity(self):
        equity = self.__rawEquity/self.__iterations
        return equity

#used to determine equity of hands by running hundreds of iterations
class HandComparison:
    __deck = None #of type Deck
    __deadCards = []
    __board = None #of type Board
    __hands = [] #of type HandData
    __handAnalyzer = None #of type HandAnalyzer
    __iterations = 1000

    def __init__(self, hands, iterations, board=None):
        self.__board = board
        self.__iterations = iterations

        dead_cards = []
        if board:
            dead_cards.append(board.getBoard())
        for hand in hands:
            self.__hands.append(HandData(hand))
            dead_cards += hand.getCards()

        self.__deadCards = dead_cards
        self.__deck = Deck.Deck(dead_cards)

    #takes availableCards and a initial board state and generates a full board
    def generateBoard(self, ac, board):
        while len(board.getBoard()) < 5:
            if not board:
                board = Board.Board(ac.getTopCard(), ac.getTopCard(), ac.getTopCard())
            elif len(self.__board.getBoard()) == 3:
                board.setTurn(self.__deck.getTopCard())
            elif len(self.__board.getBoard()) == 4:
                board.setRiver(self.__deck.getTopCard())
        return board

    def getWinner(self, board, hand1, hand2):
        ha = HandAnalyzer.HandAnalyzer()
        bh1 = ha.calculateBestHand()
        bh2 = ha.calculateBestHand()
        winner = ha.calculateWinner(bh1, bh2)
        return winner

    def updateEquity(self, hand, winner):
        if winner:
            hand.addRawEquity(100)
            hand.incrementIterations()
        elif not winner:
            hand.incrementIterations()

    def run(self):
        it = 0
        while it < self.__iterations:
            availableCards = self.__deck #resets deck before each iteration
            board = self.generateBoard(availableCards, self.__board) #resets board before each iteration

            winner = self.getWinner()
            for hand in self.__hands:
                if hand == winner:
                    self.updateEquity(hand, True)
                else:
                    self.updateEquity(hand, False)

            it += 1


comparison = HandComparison(board1, [hand1, hand2])
comparison.run()


