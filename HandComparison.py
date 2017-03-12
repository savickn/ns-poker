__author__ = 'Nick'

import HandPreflop, Board, Deck, HandAnalyzer

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
    __iterations = None

    def __init__(self, hands, iterations=1000, board=None):
        assert len(hands) >= 2

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
        if not board:
            board = Board.Board(ac.getTopCard(), ac.getTopCard(), ac.getTopCard())
        if board and len(board.getCards()) == 3:
            board.setTurn(self.__deck.getTopCard())
        if board and len(board.getCards()) == 4:
            board.setRiver(self.__deck.getTopCard())
        return board

    def getWinner(self, board, hand1, hand2):
        ha1 = HandAnalyzer.HandAnalyzer(hand1, board)
        ha2 = HandAnalyzer.HandAnalyzer(hand2, board)
        winner = HandAnalyzer.HandAnalyzer.compareHands(ha1.getBestHand(), ha2.getBestHand())

        if winner == hand1:
            print(hand1)
        elif winner == hand2:
            print(hand2)
        elif winner == 'Split':
            print()

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

board1 = Board.Board(Deck.king_clubs, Deck.four_spades, Deck.six_diamonds)
hand1 = HandPreflop.HoldemHand(Deck.ace_clubs, Deck.eight_clubs)
hand2 = HandPreflop.HoldemHand(Deck.ten_hearts, Deck.ten_diamonds)

comparison = HandComparison([hand1, hand2])
comparison.run()


