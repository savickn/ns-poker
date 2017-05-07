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


valueToBluffFrequencies = {
    'Flop': {

    },
    'Turn': {

    },
    'River': {

    }
}

callingFrequencies = {
    'Full-Pot': 0.5,
    '0.75-Pot': 0.57,
    'Half-Pot': 0.66
}

potOdds = {

}


#used to rank hands within a range to determine which X% should be called vs. a pot-size bet/etc
class GtoSolver:

    def __init__(self, range, board):
        self.__range = range #must be a Range obj
        self.__board = board #must be a list of Card objects
        self.__madeHands = self.analyzeBoard() #an array of BestHand objects
        self.checkRep()

    #poker pot odds
    def calculatePotOdds(self, bet, pot):
        return bet/(pot + bet)

    #percentage chance to make a hand by the next street
    def calculateOutPercentage(self, outs, liveCards):
        return outs/liveCards

    #for determining which hands to use for calling bets (e.g. getTopX(50) for calling pot-size bet)
    def getTopX(self, x):
        cutoff = math.ceil(len(self.__madeHands)/(100/x))
        hands = self.__madeHands[-cutoff:]
        return hands

    #used to determine which hands are strong enough to value bet
    def determineValueBets(self):
        print()

    #used to determine which hands make good  bluffs
    def determineBluffs(self):
        print()

    #used to determine which cards hurt a specific Range (good for bluffing on)
    def determineScareCards(self):
        print()

    #used to determine which range is ahead in a specific situation (e.g. BB-call has lots of SCs and suited Aces while SB-call has very few)
    def calculateStrongRange(self, board, r1, r2):
        print()

    #used to determine calling/raising/folding ranges of BB
    def bbRangeBuilder(self):
        print()

    #for determining value/bluff proportions (e.g. 66/33 Value to Bluff ratio on the River)
    def getValueBluffRange(self, state, betSize):
        obj = {}
        if state == 'Flop':
            obj['Half-Pot'] = self.getTopX(75)
            obj['Full-Pot'] = self.getTopX(67)
            obj['2x-Pot'] = self.getTopX(60)
        elif state == 'Turn':
            obj['Half-Pot'] = self.getTopX(75)
            obj['Full-Pot'] = self.getTopX(67)
            obj['2x-Pot'] = self.getTopX(60)
        elif state == 'River':
            obj['Half-Pot'] = self.getTopX(75)
            obj['Full-Pot'] = self.getTopX(67)
            obj['2x-Pot'] = self.getTopX(60)
        return obj

    #creates an array of 'X' madeHands from an array of 'X' PreflopHands
    def analyzeBoard(self):
        madeHands = []
        for hand in self.__range.getHands():
            ha = HandAnalyzer.HandAnalyzer(hand, self.__board)
            madeHands.append(ha.getBestHand())

        madeHands.sort() #this creates the unexplained printing of HighCard hands
        #Helpers.sortBestHands(madeHands)
        return madeHands

    #used to determine which Turn cards will benefit your range and which will be detrimental
    def calculateTurnLikeliness(self):
        print()

    def checkRep(self):
        assert  isinstance(self.__range, Range.Range)

b = Board.Board(*[Data.ace_clubs, Data.ace_spades, Data.four_diamonds])
d = Deck.Deck(b.getCards(), True)

selected = Deck.preflopHands['AKo'] + Deck.preflopHands['AKs'] + Deck.preflopHands['54s'] + Deck.preflopHands['98s']
r = Range.Range(selected)


gto = GtoSolver(r, b)
best50 = gto.getTopX(10)
for x in best50:
    x.printAsString()





#def get_equity(self, hero, villain, board=[]):
#    assert len(board) in range(3, 6)
#    raw_equity = 0
#    avg_equity = 0
#    for x in range(1, self.__iterations + 1):
#        raw_equity += self.run_iteration()
#    avg_equity = raw_equity/self.__iterations
#    return avg_equity

    #def run(self, hand):
    #    deadCards = self.__board + hand.getCards()
    #    deck = Deck.Deck(deadCards)
    #    deck.shuffleDeck()