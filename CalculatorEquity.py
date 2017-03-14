__author__ = 'Nick'

import HandPreflop, Board, Deck, HandAnalyzer

#holds equity information for a single hand
class Equity:
    __hand = None
    __count = 0
    __equity = 0

    def __init__(self, hand):
        self.__hand = hand

    def getHand(self):
        return self.__hand

    def updateEquity(self, equity):
        self.__equity += equity
        self.__count += 1

    def getEquity(self):
        return self.__equity/self.__count

    def toString(self):
        return '{hand}-{equity}'.format(hand=self.__hand.toString(), equity=self.getEquity())

#used to determine equity of single hands vs. one another (e.g. player1 vs player2 vs player3) by running hundreds of iterations
class EquityCalculator:
    __deck = None #of type Deck
    __board = None #of type Board
    __hands = [] #of type Equity
    __iterations = None
    __equitySplit = None

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

    #takes list of availableCards and an initial Board object and generates a full board
    def generateBoard(self, ac, board):
        if not board:
            board = Board.Board(ac.getTopCard(), ac.getTopCard(), ac.getTopCard())
        if board and len(board.getCards()) == 3:
            board.setTurn(self.__deck.getTopCard())
        if board and len(board.getCards()) == 4:
            board.setRiver(self.__deck.getTopCard())
        return board

    #helper method for determining the equity distribution in split pots
    def calculateEquitySplit(self, winners):
        equity = 100 / len(winners)
        return equity

    #returns an array of hands that have won/tied, takes a array of 5 Cards (board) and an array of objs of type PreflopHand (hands)
    def determineWinner(self, board, hands):
        analyzers = {}
        it = 1
        for hand in hands:
            analyzers['hand' + str(it)] = HandAnalyzer.HandAnalyzer(hand, board)
            it += 1

        winners = None
        for key, value in analyzers.items():
            if not winners:
                winners = [value]
            else:
                w = HandAnalyzer.HandAnalyzer.compareHands(value.getBestHand(), winners[0].getBestHand())
                if w == 'Split Pot':
                    winners.append(value)
                else:
                    winners = [value]
        self.__equitySplit = self.calculateEquitySplit(winners)
        return winners

    def updateEquity(self, hand, equity):
        hand.updateEquity(equity)

    def run(self):
        hands = []
        for eq in self.__hands:
            hands.append(eq.getHand())

        for x in range(self.__iterations):
            availableCards = self.__deck #creates a new Deck before each iteration
            availableCards.shuffleDeck() #shuffles Deck in each iteration
            board = self.generateBoard(availableCards, self.__board) #creates a new Board before each iteration

            winners = self.determineWinner(board, hands) #sets 'equitySplit' abd returns winning hands
            print(winners)
            for hand in self.__hands:
                print(hand)
                if hand.getHand() in winners:
                    self.updateEquity(hand, self.__equitySplit)
                else:
                    self.updateEquity(hand, 0)
                print(hand.toString())

    ############# UTILITY METHODS ##############

    def checkRep(self):
        assert len(self.__hands) >= 2


board1 = Board.Board(Deck.king_clubs, Deck.four_spades, Deck.six_diamonds) #Kc4s6d
hand1 = HandPreflop.HoldemHand(Deck.ace_clubs, Deck.eight_clubs) #A8c
hand2 = HandPreflop.HoldemHand(Deck.ten_hearts, Deck.ten_diamonds) #ThTd
hand3 = HandPreflop.HoldemHand(Deck.jack_hearts, Deck.nine_hearts) #J9h
hand4 = HandPreflop.HoldemHand(Deck.six_spades, Deck.five_spades) #65s
hand5 = HandPreflop.HoldemHand(Deck.queen_hearts, Deck.jack_clubs) #QhJc

comparison = EquityCalculator([hand1, hand2], board1, 1)
comparison.run()


