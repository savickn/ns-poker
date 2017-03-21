__author__ = 'Nick'

import Deck, Board, Range, HandAnalyzer, HandBest, Data
import Helpers
import operator, math

potBet = 100
threeQuarterBet = 75
twoThirdBet = 66
halfBet = 50
oneThirdBet = 33
oneQuarterBet = 25


#used to rank hands within a range to determine which X% should be called vs. a pot-size bet/etc
class GtoSolver:

    def __init__(self, range, board):
        self.__range = range #must be a Range obj
        self.__board = board #must be a list of Card objects
        self.__madeHands = self.analyzeBoard() #an array of BestHand objects

        self.checkRep()

    #for determining which hands to use for calling bets (e.g. getTopX(50) for calling pot-size bet)
    def getTopX(self, x):
        cutoff = math.ceil(len(self.__madeHands)/(100/x))
        hands = self.__madeHands[-cutoff:]
        return hands

    #for determining which hands to bet for value
    def getValueRange(self):
        print()

    #for determining which hands to use as bluffs
    def getBluffRange(self):
        print()

    #creates an array of 'X' madeHands from an array of 'X' PreflopHands
    def analyzeBoard(self):
        madeHands = []
        for hand in self.__range.getHands():
            ha = HandAnalyzer.HandAnalyzer(hand, self.__board)
            madeHands.append(ha.getBestHand())

        for h in madeHands:
            h.printAsString()

        madeHands.sort()

        #Helpers.sortBestHands(madeHands)

        for h in madeHands:
            h.printAsString()

        #madeHands.sort() #this creates the unexplained printing of HighCard hands
        return madeHands

    #used to determine which Turn cards will benefit your range and which will be detrimental
    def calculateTurnLikeliness(self):
        print()

    #def run(self, hand):
    #    deadCards = self.__board + hand.getCards()
    #    deck = Deck.Deck(deadCards)
    #    deck.shuffleDeck()

    def checkRep(self):
        assert  isinstance(self.__range, Range.Range)

b = Board.Board(*[Data.ace_clubs, Data.ace_spades, Data.four_diamonds])
d = Deck.Deck(b.getCards(), True)

selected = Deck.preflopHands['AKo'] + Deck.preflopHands['AKs'] + Deck.preflopHands['54s'] + Deck.preflopHands['98s']
r = Range.Range(selected)


gto = GtoSolver(r, b)
best50 = gto.getTopX(50)


#def get_equity(self, hero, villain, board=[]):
#    assert len(board) in range(3, 6)
#    raw_equity = 0
#    avg_equity = 0
#    for x in range(1, self.__iterations + 1):
#        raw_equity += self.run_iteration()
#    avg_equity = raw_equity/self.__iterations
#    return avg_equity
