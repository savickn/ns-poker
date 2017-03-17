__author__ = 'Nick'

import Board, HandPreflop, HandBest
import HandPair, HandTP, HandTrips, HandStraight, HandFlush, HandFH, HandQuads, HandSF, HandHC
import Helpers, Deck
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

### FULLY WORKING ###

#used to determine the different types of hands that can be made based on the board + hand, including the best possible hand
class HandAnalyzer:
    def __init__(self, hand, board, toPrint=False):
        self.__hand = hand #must be of type PreflopHand
        self.__board = board #must be of type Board
        self.__availableCards = hand.getCards() + board.getCards() #a List of cards contained with '__hand' and '__board'
        self.__bestHand = None #must be of type HandBest

        #pair-type hands
        self.__quads = []
        self.__fullHouses = []
        self.__trips = []
        self.__twoPairs = []
        self.__pairs = []

        #straight-flush-type hands
        self.__straightFlushes = []
        self.__sf_gutshot_draws = []
        self.__sf_open_ended_draws = []

        #flush-type hands
        self.__flushes = []
        self.__flushDraws = []
        self.__backdoorFDs = []

        #straight-type hands
        self.__straights = []
        self.__gutterDraws = []
        self.__openEndedDraws = []
        self.__backdoorGDs = []
        self.__backdoorOEDs = []

        #missed hands
        self.__overcards = []
        self.__nothing = [] #includes 1 overcard hands and 0 overcard hands

        #blockers
        self.__straightBlockers = []
        self.__flushBlockers = []
        self.__nutBlockers = [] #meaning hands that block strong hands, don't want to raise for value if u block strong hands

        try:
            self.checkRep()
        except AssertionError:
            print('CheckRep failed! This class is not valid.')

        self.analyzePairedHands()
        self.analyzeStraights()
        self.analyzeFlushes()
        self.calculateBestHand()

        if toPrint:
            self.printAnalysis()
            self.printAvailableCards()
            self.printBestHand()

    def checkRep(self):
        assert isinstance(self.__hand, HandPreflop.PreflopHand)
        assert isinstance(self.__board, Board.Board)
        assert len(set(self.__board.getCards()) & set(self.__hand.getCards())) == 0
        assert len(self.__availableCards) > 5

    def getBestHand(self):
        return self.__bestHand

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
                    #print('{card} makes a pair.'.format(card=card.toString()))
                    self.__pairs.append(pair)

            elif len(temp_hand) == 3:
                trips = HandTrips.Trips(temp_hand, temp_hand[0].getHighValue())
                if not Helpers.inCollection(trips, self.__trips):
                    #print('{card} makes trips.'.format(card=card.toString()))
                    self.__trips.append(trips)

            elif len(temp_hand) == 4:
                quads = HandQuads.Quads(temp_hand, temp_hand[0].getHighValue())
                if not Helpers.inCollection(quads, self.__quads):
                    #print('{card} makes quads.'.format(card=card.toString()))
                    self.__quads.append(quads)
            else:
                #print('{card} does not make a pair, trips, or quads.'.format(card=card.toString()))
                continue

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
                elif (t.getPrimaryValue() < trips.getPrimaryValue()) and ((pair is None) or (t.getPrimaryValue() > pair.getPrimaryValue())):
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
    def analyzeStraights(self, checkDraws=False):
        suit = Helpers.getRelevantSuit(self.__availableCards)
        cards = Helpers.removePairs(self.__availableCards, suit)
        sortedDeque = deque(Helpers.sortCards(cards, False))

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

        #check for straight draws
        #if checkDraws:



    #Helper function for extracting the best possible flush
    def extractBestFlush(self, cards):
        cards.sort(key=lambda card: card.getHighValue(), reverse=True)
        self.__flushes.append(HandFlush.Flush(cards[:5], cards[0].getHighValue()))

    #extracts all possible flushes from availableCards (required to calc possible straight_flushes)
    def analyzeFlushes(self, checkDraws=False):
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

        if len(spades) >= 5:
            self.extractBestFlush(spades)
        elif len(clubs) >= 5:
            self.extractBestFlush(clubs)
        elif len(hearts) >= 5:
            self.extractBestFlush(hearts)
        elif len(diamonds) >= 5:
            self.extractBestFlush(diamonds)

        if checkDraws and (len(self.__availableCards) < 7):
            if len(spades) == 4:
                self.__flushDraws.append(spades)
            elif len(clubs) == 4:
                self.extractBestFlush(clubs)
            elif len(hearts) == 4:
                self.extractBestFlush(hearts)
            elif len(diamonds) == 4:
                self.extractBestFlush(diamonds)

        if checkDraws and (len(self.__availableCards) < 6):
            if len(spades) == 3:
                self.__flushDraws.append(spades)
            elif len(clubs) == 3:
                self.extractBestFlush(clubs)
            elif len(hearts) == 3:
                self.extractBestFlush(hearts)
            elif len(diamonds) == 3:
                self.extractBestFlush(diamonds)

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
            self.__bestHand = HandBest.HandBest(self.__straightFlushes[0])
            return

        if len(self.__quads) > 0:
            highCards = self.calculateHighCards(self.__quads[0].getCards(), self.__quads[0].getLength())
            self.__bestHand = HandBest.HandBest(self.__quads[0], highCards)
            return

        if len(self.__fullHouses) > 0:
            self.__bestHand = HandBest.HandBest(self.__fullHouses[0])
            return

        if len(self.__flushes) > 0:
            self.__bestHand = HandBest.HandBest(self.__flushes[0])
            return

        if len(self.__straights) > 0:
            self.__bestHand = HandBest.HandBest(self.__straights[0])
            return

        if len(self.__trips) > 0:
            highCards = self.calculateHighCards(self.__trips[0].getCards(), self.__trips[0].getLength())
            self.__bestHand = HandBest.HandBest(self.__trips[0], highCards)
            return

        if len(self.__twoPairs) > 0:
            highCards = self.calculateHighCards(self.__twoPairs[0].getCards(), self.__twoPairs[0].getLength())
            self.__bestHand = HandBest.HandBest(self.__twoPairs[0], highCards)
            return

        if len(self.__pairs) > 0:
            pair = self.__pairs[0]
            highCards = self.calculateHighCards(pair.getCards(), pair.getLength())
            self.__bestHand = HandBest.HandBest(pair, highCards)
            return

        #sets highCards if no higher hand is made (e.g. not even a Pair)
        if self.__bestHand is None:
            highCards = self.calculateHighCards([], 0)
            self.__bestHand = HandBest.HandBest(highCards)


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
        print('HAND ANALYSIS')
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

    def printAvailableCards(self):
        print('############ PREFLOP HAND ############')
        for c in self.__hand.getCards():
            print(c.toString())

        print('############ BOARD #############')
        for c in self.__board.getCards():
            print(c.toString())

        print('############ AVAILABLE CARDS ###########')
        for c in self.__availableCards:
            print(c.toString())

    def printBestHand(self):
        print('############# BEST HAND ############')
        self.__bestHand.printAsString()
        print('############# END OF ANALYSIS ##############')



hand = HandPreflop.HoldemHand(
    [Deck.ace_clubs,
    Deck.king_spades])

#gutshot straight draw
board = Board.Board(
    Deck.six_spades,
    Deck.three_clubs,
    Deck.four_diamonds,
    Deck.five_hearts,
    Deck.jack_spades)

ha = HandAnalyzer(hand, board, True)
