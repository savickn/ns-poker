__author__ = 'Nick'

import Deck, Board, Range, HandAnalyzer


potBet = 100
threeQuarterBet = 75
twoThirdBet = 66
halfBet = 50
oneThirdBet = 33
oneQuarterBet = 25


#used to rank hands within a range to determine which X% should be called vs. a pot-size bet/etc
class GtoSolver:

    def __init__(self, range, board):
        self.__bestHands = [] #an array of BestHand objects
        self.__range = range #must be a Range obj
        self.__numberOfHands = range.getLength()
        self.__board = board #must be a list of

    #for calling pot-size bets
    def getTop50(self):
        print()

    #for calling half-pot bets
    def getTop66(self):
        print()

    def getValueRange(self):
        print()

    def getBestBluffs(self):
        print()


    #creates an array of 'X' bestHands from an array of 'X' PreflopHands
    def analyzerBoard(self):
        bestHands = []
        for hand in self.__range.getHands():
            ha = HandAnalyzer.HandAnalyzer(hand, self.__board)
            bestHands.append(ha.getBestHand())
        bestHands.sort()
        self.__bestHands = bestHands

    #used to determine which Turn cards will benefit your range and which will be detrimental
    def calculateTurnLikeliness(self):
        print()


    def run_iteration(self, hand):
        deadCards = self.__board + hand.getCards()
        deck = Deck.Deck(deadCards)
        deck.shuffleDeck()







#def get_equity(self, hero, villain, board=[]):
#    assert len(board) in range(3, 6)
#    raw_equity = 0
#    avg_equity = 0
#    for x in range(1, self.__iterations + 1):
#        raw_equity += self.run_iteration()
#    avg_equity = raw_equity/self.__iterations
#    return avg_equity
