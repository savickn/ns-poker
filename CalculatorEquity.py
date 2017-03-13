__author__ = 'Nick'

import HandPreflop, Board, Deck, HandAnalyzer

#holds equity information for a single hand
class Equity:
    __hand = None
    __iterations = 0
    __rawEquity = 0
    __avgEquity = 0

    def __init__(self, hand):
        self.__hand = hand

    def getHand(self):
        return self.__hand

    def addRawEquity(self, equity):
        self.__rawEquity += equity
        self.__iterations += 1

    def calcEquity(self):
        self.__avgEquity = self.__rawEquity/self.__iterations
        return self.__avgEquity

#used to determine equity of single hands vs. one another (e.g. player1 vs player2 vs player3) by running hundreds of iterations
class EquityCalculator:
    __deck = None #of type Deck
    __board = None #of type Board
    __hands = [] #of type HandData
    __iterations = None

    def __init__(self, hands, board=None, iterations=1000):
        self.__board = board
        self.__iterations = iterations

        dead_cards = []
        if board:
            dead_cards.append(board.getCards())
        for hand in hands:
            self.__hands.append(Equity(hand))
            dead_cards += hand.getCards()

        self.__deck = Deck.Deck(dead_cards)
        self.checkRep()

    #takes availableCards and a initial board state and generates a full board
    def generateBoard(self, ac, board):
        if not board:
            board = Board.Board(ac.getTopCard(), ac.getTopCard(), ac.getTopCard())
        if board and len(board.getCards()) == 3:
            board.setTurn(self.__deck.getTopCard())
        if board and len(board.getCards()) == 4:
            board.setRiver(self.__deck.getTopCard())
        return board

    #returns an array of hands that have won/tied, takes a array of 5 Cards (board) and an array of objs of type PreflopHand (hands)
    def determineWinner(self, board, hands):
        analyzers = {}
        it = 1
        for hand in hands:
            analyzers['hand' + str(it)] = HandAnalyzer.HandAnalyzer(hand.getCards(), board.getCards())
            it += 1

        winner = None
        for key, value in analyzers.items():
            print('{key}-{value}'.format(key=key, value=value))

            if winner is None:
                winner = [value]
            else:
                winner = HandAnalyzer.HandAnalyzer.compareHands(value.getBestHand(), winner.getBestHand())
        return winner

    def updateEquity(self, hand, equity):
        hand.addRawEquity(equity)

    def run(self):
        hands = []
        for eq in self.__hands:
            hands.append(eq.getHand())

        for x in range(self.__iterations):
            availableCards = self.__deck #resets deck before each iteration
            board = self.generateBoard(availableCards, self.__board) #resets board before each iteration

            winner = self.determineWinner(board, hands)
            for hand in self.__hands:
                if hand.getHand() == winner:
                    self.updateEquity(hand, True)
                else:
                    self.updateEquity(hand, False)

    ############# UTILITY METHODS ##############

    def checkRep(self):
        assert len(self.__hands) >= 2


board1 = Board.Board(Deck.king_clubs, Deck.four_spades, Deck.six_diamonds) #Kc4s6d
hand1 = HandPreflop.HoldemHand(Deck.ace_clubs, Deck.eight_clubs) #A8c
hand2 = HandPreflop.HoldemHand(Deck.ten_hearts, Deck.ten_diamonds) #ThTd
hand3 = HandPreflop.HoldemHand(Deck.jack_hearts, Deck.nine_hearts) #J9h
hand4 = HandPreflop.HoldemHand(Deck.six_spades, Deck.five_spades) #65s
hand5 = HandPreflop.HoldemHand(Deck.queen_hearts, Deck.jack_clubs) #QhJc

comparison = EquityCalculator([hand1, hand2], board1)
comparison.run()


