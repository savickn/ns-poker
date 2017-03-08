__author__ = 'Nick'

import Deck, Hand, HandPair, HandTP, HandTrips, HandStraight, HandFlush, HandQuads, HandSF
import Helpers
from collections import deque

handRankings = {
    'Z': 9,
    'Q': 8,
    'H': 7,
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
    __full_houses = []
    __trips = []
    __two_pairs = []
    __pairs = []

    #straight-flush-type hands
    __straight_flushes = []
    __sf_gutshot_draws = []
    __sf_open_ended_draws = []

    #flush-type hands
    __flushes = []
    __flush_draws = []
    __backdoor_flush_draws = []

    #straight-type hands
    __straights = []
    __gutshot_draws = []
    __open_ended_draws = []
    __backdoor_gutshot_draws = []
    __backdoor_open_ended_draws = []

    __overcards = []
    __nothing = [] #includes 1 overcard and 0 overcards

    #blockers
    __straight_blockers = []
    __flush_blockers = []
    __nut_blockers = [] #meaning hands that block strong hands, don't want to raise for value if u block strong hands


    def __init__(self, hand, board):
        self.__hand = hand
        self.__board = board
        self.__availableCards = board + hand

        self.checkRep()

    def getBestHand(self):
        return self.__bestHand

    #extracts all pairs/trips/quads from availableCards
    def analyzePairedHands(self):
        for card in self.__availableCards:
            temp_hand = [card]

            for card2 in self.__availableCards:
                if card2 == card:
                    continue
                if (card.getHighValue() == card2.getHighValue()):
                    print('{card} matched {card2}. Therefore, {card2} was added to temp_hand.'.format(card2=card2.toString(),
                                                                                                           card=card.toString()))
                    temp_hand.append(card2)

            if len(temp_hand) == 2:
                pair = HandPair.Pair(temp_hand)
                if not Helpers.inCollection(pair, self.__pairs):
                    print('{card} makes a pair.'.format(card=card.toString()))
                    self.__pairs.append(pair)

            elif len(temp_hand) == 3:
                trips = HandTrips.Trips(temp_hand)
                if not Helpers.inCollection(trips, self.__trips):
                    print('{card} makes trips.'.format(card=card.toString()))
                    self.__trips.append(trips)

            elif len(temp_hand) == 4:
                quads = HandQuads.Quads(temp_hand)
                if not Helpers.inCollection(quads, self.__quads):
                    print('{card} makes quads.'.format(card=card.toString()))
                    self.__quads.append(quads)
            else:
                print('{card} does not make a pair, trips, or quads.'.format(card=card.toString()))

    #extracts all possible straights from availableCards (required to calc possible straight_flushes)
    def analyzeStraights(self, draws=False):
        sorted_cards = deque(Helpers.sortCards(self.__availableCards, False))
        list_length = len(sorted_cards)

        it = 0
        while it < list_length:
            if Helpers.isStraight(sorted_cards):
                straight = list(sorted_cards)
                relevant_cards = straight[-5:]
                break
            else:
                sorted_cards.rotate(1)
                it += 1

    #Helper function for analyzing flushes
    def extractFlushes(self, cards):
        cards.sort(key=lambda card: card.getHighValue(), reverse=True)
        suit = cards[0].getSuit()
        if len(cards) == 5:
            self.__flushes.append(HandFlush.Flush(cards, suit))
        if len(cards) == 6:
            self.__flushes.append(HandFlush.Flush(cards[:5], suit))
            self.__flushes.append(HandFlush.Flush(cards[1:6], suit))
        if len(cards) == 7:
            self.__flushes.append(HandFlush.Flush(cards[:5], suit))
            self.__flushes.append(HandFlush.Flush(cards[1:6], suit))
            self.__flushes.append(HandFlush.Flush(cards[2:7], suit))

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
            self.extractFlushes(spades)
        elif(len(clubs) >= 5):
            self.extractFlushes(clubs)
        elif(len(hearts) >= 5):
            self.extractFlushes(hearts)
        elif(len(diamonds) >= 5 ):
            self.extractFlushes(diamonds)
        else:
            print('This hand does not make a flush.')

    #determines the winner between two separate player's hands
    def calculateWinner(self, hand1, hand2):
        winner = None
        if handRankings[hand1.getPrefix()] > handRankings[hand2.getPrefix()]:
            winner = hand1
        elif handRankings[hand2.getPrefix()] > handRankings[hand1.getPrefix()]:
            winner = hand2
        else:
            winner = hand1.compare(hand2)
        return winner


    def hasStraightFlush(self):
        sf = HandStraightFlush.SF()
        for hand in self.__flushes:
            if Helpers.isStraight(hand):
                self.__bestHand = hand
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



    #determines the best possible hand that a player's hole cards can make given the board
    def calculateBestHand(self, *input_cards):
        if input_cards:
            cards = input_cards
        else:
            cards = self.__availableCards

        if self.hasStraightFlush():


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

        if self.calculate_high_cards(sorted_cards, 5):
            return self.__bestHand

        #calculates remaining cards using symmetrical difference
        #remaining_cards = set(relevant_cards) ^ set(initial_cards)
        #remaining_cards = list(remaining_cards)

        #best_hand = calculate_high_cards(relevant_cards, remaining_cards)

    ##################### Helpers

    def calculate_high_cards(self, made_hand, cards) :
        #while len(made_hand) < 5 :
        #    made_hand.append(sorted_cards.pop(0))
        return made_hand

    ####################### Individual Hand Checks


    def checkRep(self):
        assert len(self.__availableCards) > 5
        assert len(self.__board) > 3
        assert len(self.__hand) in [2, 4]

        #if len(cards) > 7 or len(cards) < 5:
        #    raise Exception('HandAnalyzer failed to init')

    #helper for printing hand analyzes
    def printCategory(self, hands, category, abbr):
        print('##### {category} ####'.format(category=category))
        it = 1
        for hand in hands:
            print('##### {abbr}-{num} #####'.format(abbr=abbr, num=it))
            it += 1
            for card in hand:
                print(card.toString())

    def printAnalysis(self):
        self.printCategory(self.__straight_flushes, 'Straight Flushes', 'SF')
        self.printCategory(self.__quads, 'Quads', 'Q')
        self.printCategory(self.__full_houses, 'Full Houses', 'FH')
        self.printCategory(self.__flushes, 'Flushes', 'F')
        self.printCategory(self.__straights, 'Straights', 'S')
        self.printCategory(self.__trips, 'Trips', 'T')
        self.printCategory(self.__two_pairs, 'Two Pairs', 'TP')
        self.printCategory(self.__pairs, 'Pairs', 'P')

        self.printCategory(self.__flush_draws, 'Flush Draws', 'FD')
        self.printCategory(self.__gutshot_draws, 'Gutshots Draws', 'SD')
        self.printCategory(self.__open_ended_draws, 'Open-Ended Draws', 'OED')

        self.printCategory(self.__overcards, 'Overcards', 'OC')
        self.printCategory(self.__nothing, 'Nothing', 'N')



hand = [
    Deck.ace_spades,
    Deck.two_spades
]
board = [
    Deck.ace_hearts,
    Deck.five_clubs,
    Deck.six_diamonds,
    Deck.ten_hearts,
    Deck.jack_clubs
]

ha = HandAnalyzer(hand, board)
ha.analyzePairedHands()







