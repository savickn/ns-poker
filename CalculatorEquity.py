__author__ = 'Nick'

import HandPreflop, Board, Data, Deck, HandAnalyzer, HandEquity, HandBest

# can simplify equity calculations by using probability (e.g. flush draw vs. trips)
# would have 35% to beat trips but trips would also improve to full house 35% of the time (e.g. 35% of 35% == 12%)

####### FULLY WORKING #######
#used to determine equity of single hands vs. one another (e.g. player1 vs player2 vs player3) by running hundreds of iterations
class EquityCalculator:
    __equitySplit = None

    def __init__(self, hands, board=None, iterations=1000):
        self.__board = board #must be a Board object
        self.__iterations = iterations
        self.__equities = [] #nust contain Equity objs

        dead_cards = []
        for c in board.getCards():
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

        winners = []
        for key, value in analyzers.items():
            if len(winners) == 0:
                winners = [value.getBestHand()]
            else:
                v = value.getBestHand()
                w = HandBest.HandBest.compare(v, winners[0])
                if w == 0:
                    winners.append(v)
                elif w == 1:
                    winners = [v]

        self.__equitySplit = self.calculateEquitySplit(len(winners))
        return winners #should be an array of BestHands

    #updates a hand's equity via its Equity object
    def updateEquity(self, eqObj, equity):
        eqObj.updateEquity(equity)

    def printEquities(self):
        print('### Equities ###')
        print('EQ SPLIT: {split}'.format(split=self.__equitySplit))
        for eq in self.__equities:
            print(eq)

    #main function for determining equity
    def run(self):
        hands = []
        for eq in self.__equities:
            hands.append(eq.getHand())

        for x in range(self.__iterations):
            deck = Deck.Deck(self.__deadCards)
            deck.shuffleDeck()
            board = Board.Board.generateBoard(deck, self.__board.getCards()) #creates a new Board before each iteration
            print(board)

            winners = self.determineWinner(board, hands) #sets 'equitySplit' and returns winning BestHand
            for eq in self.__equities:
                matched = False
                for w in winners:
                    if HandBest.HandBest.matchesWinningHand(w, eq.getHand(), board):
                        matched = True
                if matched:
                    self.updateEquity(eq, self.__equitySplit)
                else:
                    self.updateEquity(eq, 0)

            #print('# WINNER #')
            #winner.printAsString()
            self.printEquities()

    ############# UTILITY METHODS ##############

    def checkRep(self):
        assert len(self.__equities) >= 2


board1 = Board.Board(Data.king_clubs, Data.four_spades, Data.six_diamonds, Data.king_spades, Data.eight_diamonds) #Kc4s6dKs8d
board2 = Board.Board(Data.king_clubs, Data.four_spades, Data.six_diamonds) #Kc4s6d

hand1 = HandPreflop.HoldemHand([Data.ace_clubs, Data.eight_clubs]) #A8c
hand2 = HandPreflop.HoldemHand([Data.ten_hearts, Data.ten_diamonds]) #ThTd
hand3 = HandPreflop.HoldemHand([Data.jack_hearts, Data.nine_hearts]) #J9h
hand4 = HandPreflop.HoldemHand([Data.six_spades, Data.five_spades]) #65s
hand5 = HandPreflop.HoldemHand([Data.queen_hearts, Data.jack_clubs]) #QhJc
hand6 = HandPreflop.HoldemHand([Data.ace_hearts, Data.seven_spades]) #Ah7c

#glitchy when comparing 'hand1' and 'hand6'
comparison = EquityCalculator([hand1, hand6], board2, 1000)
comparison.run()






