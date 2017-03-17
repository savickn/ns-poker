__author__ = 'Nick'

import HandPreflop, Board, Deck, HandAnalyzer, HandEquity

# can simplify equity calculations by using probability (e.g. flush draw vs. trips)
# would have 35% to beat trips but trips would also improve to full house 35% of the time (e.g. 35% of 35% == 12%)

####### FULLY WORKING #######
#used to determine equity of single hands vs. one another (e.g. player1 vs player2 vs player3) by running hundreds of iterations
class EquityCalculator:
    __equitySplit = None

    def __init__(self, hands, board=[], iterations=1000):
        self.__board = board #must be list of Cards
        self.__iterations = iterations
        self.__equities = [] #nust contain Equity objs

        dead_cards = []
        for c in board:
            dead_cards.append(c)
        for hand in hands:
            self.__equities.append(HandEquity.Equity(hand))
            dead_cards += hand.getCards()

        self.__deadCards = dead_cards
        self.checkRep()

    #helper method for determining the equity distribution in split pots
    def calculateEquitySplit(self, winnerCount):
        equity = 100 / winnerCount
        return equity

    #returns the winning BestHand object, takes a array of 5 Cards (board) and an array of objs of type PreflopHand (hands)
    def determineWinner(self, board, hands):
        analyzers = {}
        it = 1
        for hand in hands:
            analyzers['hand' + str(it)] = HandAnalyzer.HandAnalyzer(hand, board, False)
            it += 1

        winner = None
        winnerCount = 0
        for key, value in analyzers.items():
            #value.getBestHand().printAsString()
            if not winner:
                winner = value.getBestHand()
                winnerCount = 1
            else:
                v = value.getBestHand()
                w = v.compare(winner)
                if w == 0:
                    winnerCount += 1
                elif w == 1:
                    winner = v
                    winnerCount = 1

        self.__equitySplit = self.calculateEquitySplit(winnerCount)
        return winner #should be of type BestHand

    #updates a hand's equity via its Equity object
    def updateEquity(self, eqObj, equity):
        eqObj.updateEquity(equity)

    def printEquities(self):
        print('### Equities ###')
        print('EQ SPLIT: {split}'.format(split=self.__equitySplit))
        for eq in self.__equities:
            print(eq.toString())

    #main function for determining equity
    def run(self):
        hands = []
        for eq in self.__equities:
            hands.append(eq.getHand())

        for x in range(self.__iterations):
            deck = Deck.Deck(self.__deadCards)
            deck.shuffleDeck()
            board = Board.Board.generateBoard(deck, self.__board) #creates a new Board before each iteration
            #board.printAsString()

            winner = self.determineWinner(board, hands) #sets 'equitySplit' and returns winning BestHand
            for eq in self.__equities:
                if eq.getHand().getCards() in winner:
                    self.updateEquity(eq, self.__equitySplit)
                else:
                    self.updateEquity(eq, 0)

            #print('# WINNER #')
            #winner.printAsString()
            self.printEquities()

    ############# UTILITY METHODS ##############

    def checkRep(self):
        assert len(self.__equities) >= 2


board1 = Board.Board(Deck.king_clubs, Deck.four_spades, Deck.six_diamonds, Deck.king_spades, Deck.eight_diamonds) #Kc4s6dKs8d
board2 = Board.Board(Deck.king_clubs, Deck.four_spades, Deck.six_diamonds) #Kc4s6d

hand1 = HandPreflop.HoldemHand([Deck.ace_clubs, Deck.eight_clubs]) #A8c
hand2 = HandPreflop.HoldemHand([Deck.ten_hearts, Deck.ten_diamonds]) #ThTd
hand3 = HandPreflop.HoldemHand([Deck.jack_hearts, Deck.nine_hearts]) #J9h
hand4 = HandPreflop.HoldemHand([Deck.six_spades, Deck.five_spades]) #65s
hand5 = HandPreflop.HoldemHand([Deck.queen_hearts, Deck.jack_clubs]) #QhJc

#comparison = EquityCalculator([hand1, hand2], board2.getCards(), 1000)
#comparison.run()






