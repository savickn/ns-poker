__author__ = 'Nick'

import Deck
import HandPair, HandTP, HandTrips, HandStraight, HandFlush, HandFH, HandQuads, HandSF
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
    __bestHand = None

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

    def __init__(self, hand, board):
        self.__hand = hand
        self.__board = board
        self.__availableCards = board + hand
        self.checkRep()

    def checkRep(self):
        #assert len(set(self.__board.getCards()) & set(self.__hand.getCards())) == 0
        assert len(self.__board) > 3
        assert len(self.__hand) in [2, 4]
        assert len(self.__availableCards) > 5

    def getBestHand(self):
        return self.__bestHand

    #determines the winner between two separate player's hands
    def compareHands(self, hand1, hand2):
        if handRankings[hand1.getPrefix()] > handRankings[hand2.getPrefix()]:
            return hand1
        elif handRankings[hand2.getPrefix()] > handRankings[hand1.getPrefix()]:
            return hand2
        elif handRankings[hand2.getPrefix()] == handRankings[hand1.getPrefix()]:
            winner = hand1.compare(hand2)
            return winner
        else:
            raise Exception('One or more hand prefixes is not valid.')

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
                    self.__straightFlushes.append(s)

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
    def calculateHighCards(self, relevant_cards, remaining_cards) :
        _relevant_cards = relevant_cards
        _remaining_cards = remaining_cards
        number_of_cards = len(relevant_cards) + len(remaining_cards)
        assert(number_of_cards > 4)

        _remaining_cards.sort(key=lambda card: card.getHighValue(), reverse=True)

        while len(_relevant_cards) < 5 :
            _relevant_cards.append(_remaining_cards.pop(0))

        assert len(_relevant_cards) == 5
        assert len(_remaining_cards) == number_of_cards - len(_relevant_cards)

        return _relevant_cards

    ################# DETERMINE BEST HAND METHOD ######################

    #determines the best possible hand that a player's hole cards can make given the board
    def calculateBestHand(self, *input_cards):
        if input_cards:
            cards = input_cards
        else:
            cards = self.__availableCards

        if self.hasStraightFlush():
            print()

        if self.hasQuads():
            return self.__bestHand

        if self.hasFullHouse():
            return self.__bestHand

        if self.hasFlush():
            return self.__bestHand

        if self.hasStraight():
            return self.__bestHand

        if self.hasTrips():
            return self.__bestHand

        if self.hasTwoPair():
            return self.__bestHand

        if self.hasPair():
            return self.__bestHand

        #if self.calculate_high_cards():
        #    return self.__bestHand

        #calculates remaining cards using symmetrical difference
        #remaining_cards = set(relevant_cards) ^ set(initial_cards)
        #remaining_cards = list(remaining_cards)

        #best_hand = calculate_high_cards(relevant_cards, remaining_cards)

    ############### Individual Hand Checks ####################

    def hasStraightFlush(self):
        sf = None
        for hand in self.__flushes:
            if Helpers.isStraight(hand):
                return

    def hasQuads(self):
        sf = None
        for hand in self.__flushes:
            if Helpers.isStraight(hand):
                self.__bestHand = hand
                return

    def hasFullHouse(self):
        sf = None
        for hand in self.__flushes:
            if Helpers.isStraight(hand):
                self.__bestHand = hand
                return

    def hasStraight(self):
        sf = None
        for hand in self.__flushes:
            if Helpers.isStraight(hand):
                self.__bestHand = hand
                return

    def hasFlush(self):
        print()

    def hasTrips(self):
        print()

    def hasTwoPair(self):
        print()

    def hasPair(self):
        print()


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


hand = [
    Deck.ace_spades,
    Deck.king_diamonds
]

#double-trips full house
board1 = [
    Deck.ace_hearts,
    Deck.five_clubs,
    Deck.ten_diamonds,
    Deck.ten_hearts,
    Deck.ten_clubs
]

#two pair
board2 = [
    Deck.king_hearts,
    Deck.five_clubs,
    Deck.six_diamonds,
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
    Deck.king_spades,
    Deck.queen_spades,
    Deck.jack_spades,
    Deck.ten_spades,
    Deck.nine_spades
]


ha = HandAnalyzer(hand, board5)
ha.analyzePairedHands() #working
ha.analyzeStraights() #glitchy, fails to recognize Straights/Straight Flushes when a pair is in the middle (might only choose one of the pair cards)
ha.analyzeFlushes() #working
ha.printAnalysis()








