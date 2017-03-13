__author__ = 'Nick'

import Deck
import HandPair, HandTP, HandTrips, HandStraight, HandFlush, HandFH, HandQuads, HandSF, HandHC
import Helpers
from collections import deque

handRankings = {
    'Z': 9,
    'Q': 8,
    'B': 7,
    'F': 6,
    'S': 5,
    'T': 4,
    'W': 3,
    'P': 2,
    'C': 1
}

#used to determine the different types of hands that can be made based on the board + hand, including the best possible hand
class HandAnalyzer:
    __hand = None
    __board = None
    __availableCards = None
    __bestHand = None #an array of objects of sub-type Hand that together add up to 5 Cards

    #pair-type hands
    __quads = []
    __fullHouses = []
    __trips = []
    __twoPairs = []
    __pairs = []

    #straight-flush-type hands
    __straightFlushes = []
    __sf_gutshot_draws = []
    __sf_open_ended_draws = []

    #flush-type hands
    __flushes = []
    __flushDraws = []
    __backdoorFDs = []

    #straight-type hands
    __straights = []
    __gutterDraws = []
    __openEndedDraws = []
    __backdoorGDs = []
    __backdoorOEDs = []

    #missed hands
    __overcards = []
    __nothing = [] #includes 1 overcard hands and 0 overcard hands

    #blockers
    __straightBlockers = []
    __flushBlockers = []
    __nutBlockers = [] #meaning hands that block strong hands, don't want to raise for value if u block strong hands

    # accepts an array of 2-4 cards (hand) and an array of 5 cards(board)
    def __init__(self, hand, board):
        self.__hand = hand
        self.__board = board
        self.__availableCards = hand + board

        try:
            self.checkRep()
        except AssertionError:
            print('CheckRep failed! This class is not valid.')

        self.analyzePairedHands()
        self.analyzeStraights()
        self.analyzeFlushes()
        self.calculateBestHand()

    def checkRep(self):
        assert len(set(self.__board) & set(self.__hand)) == 0
        assert len(self.__board) > 3
        assert len(self.__hand) in [2, 4]
        assert len(self.__availableCards) > 5

    def getBestHand(self):
        return self.__bestHand

    #determines the winner between two separate player's hands
    @staticmethod
    def compareHands(hand1, hand2):
        for x, y in hand1, hand2:
            if handRankings[x.getPrefix()] > handRankings[y.getPrefix()]:
                return hand1
            elif handRankings[y.getPrefix()] > handRankings[x.getPrefix()]:
                return hand2
            elif handRankings[x.getPrefix()] == handRankings[y.getPrefix()]:
                winner = x.compare(y)
                if winner is not None:
                    return winner
            else:
                raise Exception('One or more hand prefixes is not valid.')
        return 'Split Pot' #returns if both players hands are identical

    ############ ANALYSIS METHODS #############

    #extracts all pairs/trips/quads from availableCards, can prob be optimized better
    def analyzePairedHands(self):
        for card in self.__availableCards:
            temp_hand = [card]

            for card2 in self.__availableCards:
                if card2 == card:
                    continue
                if card.getHighValue() == card2.getHighValue():
                    #print('{card} matched {card2}. Therefore, {card2} was added to temp_hand.'.format(card=card.toString(), card2=card2.toString()))
                    temp_hand.append(card2)

            if len(temp_hand) == 2:
                pair = HandPair.Pair(temp_hand, temp_hand[0].getHighValue())
                if not Helpers.inCollection(pair, self.__pairs):
                    print('{card} makes a pair.'.format(card=card.toString()))
                    self.__pairs.append(pair)

            elif len(temp_hand) == 3:
                trips = HandTrips.Trips(temp_hand, temp_hand[0].getHighValue())
                if not Helpers.inCollection(trips, self.__trips):
                    print('{card} makes trips.'.format(card=card.toString()))
                    self.__trips.append(trips)

            elif len(temp_hand) == 4:
                quads = HandQuads.Quads(temp_hand, temp_hand[0].getHighValue())
                if not Helpers.inCollection(quads, self.__quads):
                    print('{card} makes quads.'.format(card=card.toString()))
                    self.__quads.append(quads)
            else:
                print('{card} does not make a pair, trips, or quads.'.format(card=card.toString()))

        #checks for full houses
        if (len(self.__trips) == 2) or (len(self.__trips) > 0 and len(self.__pairs) > 0):
            trips = None
            pair = None

            for p in self.__pairs:
                if (pair is None) or (p.getPrimaryValue() > pair.getPrimaryValue()):
                    pair = p

            for t in self.__trips:
                if trips is None:
                    trips = t

                #replaces old 'trips' with current 'trips' if current 'trips' > old 'trips'
                elif t.getPrimaryValue() > trips.getPrimaryValue():
                    temp = trips
                    trips = t

                    #replaces 'pair' with the old 'trips' value if 'trips' > 'pair'
                    if (pair is None) or (temp.getPrimaryValue() > pair.getPrimaryValue()):
                        pair = HandPair.Pair(temp.getCards()[:2], temp.getPrimaryValue())

                #replaces 'pair' with the current 'trips' value if current 'trips' < old 'trips' but also > 'pair'
                elif (t.getPrimaryValue() < trips.getPrimaryValue()) and ((pair == None) or (t.getPrimaryValue() > pair.getPrimaryValue())):
                    pair = HandPair.Pair(t.getCards()[:2], t.getPrimaryValue())

            if trips and pair:
                self.__fullHouses.append(HandFH.FullHouse(trips, pair))

        #checks for two pairs
        if len(self.__pairs) > 1:
            p1 = None
            p2 = None

            for p in self.__pairs:
                if p1 is None:
                    p1 = p
                elif p2 is None:
                    p2 = p
                elif p.getPrimaryValue() > p2.getPrimaryValue():
                    p2 = p

                #used to keep pairs in the correct order
                if (p1 and p2) and (p2.getPrimaryValue() > p1.getPrimaryValue()):
                    temp = p1
                    p1 = p2
                    p2 = temp

            if p1 and p2:
                self.__twoPairs.append(HandTP.TwoPair(p1, p2))

    #extracts all possible straights from availableCards (required to calc possible straight_flushes)
    def analyzeStraights(self, draws=False):
        sortedDeque = deque(Helpers.sortCards(self.__availableCards, False))

        it = 0
        while it < len(sortedDeque):
            sortedCards = list(sortedDeque)
            if Helpers.isStraight(sortedCards):
                cards = sortedCards[-5:]
                value = cards[-1].getHighValue()
                straight = HandStraight.Straight(cards, value)

                #ensures no duplicate straights are added
                if not Helpers.inCollection(straight, self.__straights):
                    self.__straights.append(straight)
            else:
                sortedDeque.rotate(1)
            it += 1

        #used to check for straight flushes
        if len(self.__straights) > 0:
            for s in self.__straights:
                if Helpers.isFlush(s.getCards()):
                    cards = s.getCards()
                    value = cards[-1].getHighValue()
                    self.__straightFlushes.append(HandSF.StraightFlush(cards, value))

    #Helper function for extracting the best possible flush
    def extractBestFlush(self, cards):
        cards.sort(key=lambda card: card.getHighValue(), reverse=True)
        self.__flushes.append(HandFlush.Flush(cards[:5], cards[0].getHighValue()))

    #extracts all possible flushes from availableCards (required to calc possible straight_flushes)
    def analyzeFlushes(self, draws=False):
        spades = []
        clubs = []
        diamonds = []
        hearts = []

        for card in self.__availableCards:
            if(card.getSuit() == 'Spades'):
                spades.append(card)
            elif(card.getSuit() == 'Hearts'):
                hearts.append(card)
            elif(card.getSuit() == 'Clubs'):
                clubs.append(card)
            elif(card.getSuit() == 'Diamonds'):
                diamonds.append(card)
            else:
                raise Exception('This card has an invalid suit.')

        if(len(spades) >= 5):
            self.extractBestFlush(spades)
        elif(len(clubs) >= 5):
            self.extractBestFlush(clubs)
        elif(len(hearts) >= 5):
            self.extractBestFlush(hearts)
        elif(len(diamonds) >= 5 ):
            self.extractBestFlush(diamonds)
        else:
            print('This hand does not make a flush.')

    #fills a given hand with high cards and returns the resulting 5 card hand... working
    def calculateHighCards(self, cards, length):
        remainingCards = []
        for c in self.__availableCards:
            if c not in cards:
                remainingCards.append(c)

        remainingCards.sort(key=lambda card: card.getHighValue(), reverse=True)
        additionalCards = 5 - length

        if additionalCards > 0:
            highCards = HandHC.HighCards(remainingCards[:additionalCards], remainingCards[0], additionalCards)
            return highCards
        else:
            raise Exception('This hand does not require any additional high cards.')

    ################# DETERMINE BEST HAND METHOD ######################

    #determines the best possible hand that a player's hole cards can make given the board
    def calculateBestHand(self):
        #sets bestHand to straight flush if it exists
        if len(self.__straightFlushes) > 0:
            self.__bestHand = [self.__straightFlushes[0]]
            return

        if len(self.__quads) > 0:
            self.__bestHand = [self.__quads[0]]
            return

        if len(self.__fullHouses) > 0:
            self.__bestHand = [self.__fullHouses[0]]
            return

        if len(self.__flushes) > 0:
            self.__bestHand = [self.__flushes[0]]
            return

        if len(self.__straights) > 0:
            self.__bestHand = [self.__straights[0]]
            return

        if len(self.__trips) > 0:
            highCards = self.calculateHighCards(self.__trips[0].getCards(), self.__trips[0].getLength())
            self.__bestHand = [self.__trips[0], highCards]
            return

        if len(self.__twoPairs) > 0:
            highCards = self.calculateHighCards(self.__twoPairs[0].getCards(), self.__twoPairs[0].getLength())
            self.__bestHand = [self.__twoPairs[0], highCards]
            return

        if len(self.__pairs) > 0:
            pair = self.__pairs[0]
            highCards = self.calculateHighCards(pair.getCards(), pair.getLength())
            self.__bestHand = [pair, highCards]
            return

        #sets highCards if no higher hand is made (e.g. not even a Pair)
        if self.__bestHand is None:
            highCards = self.calculateHighCards([], 0)
            self.__bestHand = [highCards]


    ######## PRINTING RESULTS ##############

    #helper for printing hand analyzes
    def printCategory(self, hands, category, abbr):
        print('# {category}-{count}'.format(category=category, count=len(hands)))
        it = 1
        for hand in hands:
            print('### {abbr}-{num}'.format(abbr=abbr, num=it))
            it += 1
            for card in hand.getCards():
                print('###### {card}'.format(card=card.toString()))

    def printAnalysis(self):
        self.printCategory(self.__straightFlushes, 'Straight Flushes', 'SF')
        self.printCategory(self.__quads, 'Quads', 'Q')
        self.printCategory(self.__fullHouses, 'Full Houses', 'FH')
        self.printCategory(self.__flushes, 'Flushes', 'F')
        self.printCategory(self.__straights, 'Straights', 'S')
        self.printCategory(self.__trips, 'Trips', 'T')
        self.printCategory(self.__twoPairs, 'Two Pairs', 'TP')
        self.printCategory(self.__pairs, 'Pairs', 'P')

        self.printCategory(self.__flushDraws, 'Flush Draws', 'FD')
        self.printCategory(self.__gutterDraws, 'Gutshots Draws', 'SD')
        self.printCategory(self.__openEndedDraws, 'Open-Ended Draws', 'OED')

        self.printCategory(self.__overcards, 'Overcards', 'OC')
        self.printCategory(self.__nothing, 'Nothing', 'N')

    def printBestHand(self):
        print('############# BEST HAND ############')
        for h in self.__bestHand:
            for c in h.getCards():
                print(c.toString())


hand = [
    Deck.ace_spades,
    Deck.seven_spades
]

#double-trips full house
board1 = [
    Deck.ace_hearts,
    Deck.ace_clubs,
    Deck.ten_diamonds,
    Deck.ten_hearts,
    Deck.ten_clubs
]

#two pair
board2 = [
    Deck.king_hearts,
    Deck.five_clubs,
    Deck.seven_diamonds,
    Deck.ten_hearts,
    Deck.ten_clubs
]

#flush
board3 = [
    Deck.king_spades,
    Deck.five_spades,
    Deck.six_spades,
    Deck.ten_spades,
    Deck.jack_spades
]

#straight
board4 = [
    Deck.two_spades,
    Deck.three_clubs,
    Deck.four_diamonds,
    Deck.five_hearts,
    Deck.jack_spades
]

#straight flush
board5 = [
    Deck.six_spades,
    Deck.five_spades,
    Deck.four_spades,
    Deck.three_spades,
    Deck.two_spades
]

#pair
board6 = [
    Deck.ace_hearts,
    Deck.five_spades,
    Deck.four_spades,
    Deck.three_hearts,
    Deck.ten_hearts
]

#trips
board7 = [
    Deck.ace_hearts,
    Deck.ace_clubs,
    Deck.five_spades,
    Deck.four_spades,
    Deck.three_hearts
]

#high cards
board8 = [
    Deck.king_clubs,
    Deck.six_diamonds,
    Deck.five_spades,
    Deck.jack_clubs,
    Deck.ten_diamonds
]


#all possible analysis are working
#ha = HandAnalyzer(hand, board8)
#ha.printAnalysis()
#ha.printBestHand()


