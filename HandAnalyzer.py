__author__ = 'Nick'

from PokerCalculator import Hand, HandPair, HandQuads, HandTrips, Deck
from PokerCalculator import Helpers
from collections import deque

hand_rankings = {
    'straight_flush': 9,
    'quads': 8,
    'full_house': 7,
    'flush': 6,
    'straight': 5,
    'trips': 4,
    'two_pair': 3,
    'pair': 2,
    'high_card': 1
}

#used to determine the different types of hands that can be made based on the board + hand, including the best possible hand
class HandAnalyzer:
    __hand = None
    __board = None
    __availableCards = None
    __best_hand = None

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
    __nothing = []

    def __init__(self, hand, board):
        self.__hand = hand
        self.__board = board
        self.__availableCards = board + hand

        self.checkRep()

    def getBestHand(self):
        return self.__best_hand

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
            made_hand = calculate_high_cards([], spades)
        elif(len(clubs) >= 5):
            made_hand = calculate_high_cards([], clubs)
        elif(len(hearts) >= 5):
            made_hand = calculate_high_cards([], hearts)
        elif(len(diamonds) >= 5 ):
            made_hand = calculate_high_cards([], diamonds)
        else:
            print('This hand does not make a flush.')


    def calculateWinner(self, hand1, hand2):
        print()


    def calculateBestHand(self, *input_cards):
        if input_cards:
            cards = input_cards
        else:
            cards = self.__availableCards

        #used to sort hand by value
        sorted_cards = sorted(cards, key=lambda card: card.getHighValue(), reverse=True)

        #if self.check_for_straight_flush(sorted_cards):
        #    return self.__best_hand

        bestHand = None
        while bestHand is None:
            print()

        if self.check_for_quads(sorted_cards):
            return self.__best_hand

        if self.check_for_full_house(sorted_cards):
            return self.__best_hand

        if self.check_for_flush(sorted_cards):
            return self.__best_hand

        if self.check_for_straight(sorted_cards):
            return self.__best_hand

        if self.check_for_trips(sorted_cards):
            return self.__best_hand

        if self.check_for_two_pair(sorted_cards):
            return self.__best_hand

        if self.check_for_pair(sorted_cards):
            return self.__best_hand

        if self.calculate_high_cards(sorted_cards, 5):
            return self.__best_hand

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







