__author__ = 'Nick'

from PokerCalculator import Hand, HandPair, HandQuads, HandTrips
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
    __quads = [] #should be of type Trips
    __full_houses = [] #should be of type Trips
    __trips = [] #should be of type Trips
    __two_pairs = []
    __pairs = []

    #straight-flush-type hands
    __straight_flush = None #should be of type Trips
    __sf_gutshot = None
    __sf_open_ender = None

    #flush-type hands
    __flushes = None #should be of type Trips
    __flush_draws = None
    __backdoor_flush_draws = None

    #straight-type hands
    __straight = None #should be of type Trips
    __gutshot_draw = False
    __open_ended_draw = False
    __backdoor_gutshot_draw = False
    __backdoor_open_ended_draw = False

    __overcards = None
    __nothing = None

    def __init__(self, hand, board):
        self.__hand = hand
        self.__board = board
        self.__availableCards = board.getCards() + hand.getCards()

        self.checkRep()

    def getBestHand(self):
        return self.__best_hand

    #extracts all pairs/trips/quads from availableCards
    def analyzePairedHands(self):
        relevant_cards = []

        for card1 in self.__availableCards:
            if card1 in relevant_cards:
                continue
            temp_hand = [card1]

            for card2 in self.__availableCards:
                if card2 == card1 or card2 in relevant_cards:
                    continue
                if (card1.getHighValue() == card2.getHighValue()):
                    print('{card1} matched {card2}. Therefore, {card2} was added to temp_hand.'.format(card2=card2.toString(),
                                                                                                           card1=card1.toString()))
                    temp_hand.append(card2)

            if len(temp_hand) == 2:
                pair = HandPair.Pair(temp_hand)
                if pair not in self.__pairs:
                    print('{card1} makes a pair.'.format(card1=card1.toString()))
                    self.__pairs.append(pair)

            elif len(temp_hand) == 3:
                trips = HandTrips.Trips(temp_hand)
                if trips not in self.__trips:
                    print('{card1} makes trips.'.format(card1=card1.toString()))
                    self.__trips.append(trips)

            elif len(temp_hand) == 4:
                quads = HandQuads.Quads(temp_hand)
                if quads not in self.__quads:
                    print('{card1} makes quads.'.format(card1=card1.toString()))
                    self.__quads.append(quads)
            else:
                print('{card1} does not make a pair, trips, or quads.'.format(card1=card1.toString()))

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






    def checkRep(self):
        assert len(self.__availableCards) > 5
        assert len(self.__board.getCards()) > 3
        assert len(self.__hand.getCards()) in [2, 4]

        #if len(cards) > 7 or len(cards) < 5:
        #    raise Exception('HandAnalyzer failed to init')


    def calculateWinner(self, hand1, hand2):



    def calculateBestHand(self, *input_cards):
        if input_cards:
            cards = input_cards
        else:
            cards = self.__available_cards

        #used to sort hand by value
        sorted_cards = sorted(cards, key=lambda card: card.getHighValue(), reverse=True)

        #if self.check_for_straight_flush(sorted_cards):
        #    return self.__best_hand

        bestHand = None
        while bestHand is None:


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
        remaining_cards = set(relevant_cards) ^ set(initial_cards)
        remaining_cards = list(remaining_cards)

        best_hand = calculate_high_cards(relevant_cards, remaining_cards)

    ##################### Helpers

    def calculate_high_cards(self, made_hand, cards) :
        while len(made_hand) < 5 :
            made_hand.append(sorted_cards.pop(0))

        return made_hand

    ####################### Individual Hand Checks


    def check_for_straight_flush(self, cards):
        #should be passed a flush





    def check_for_quads(self, cards) :
        initial_cards = cards
        relevant_cards = []
        remaining_cards = []

        for parent_card in cards:
            temp_hand = [parent_card]

            for card in cards:
                if (parent_card.value == card.value) and (parent_card.suit != card.suit):
                    temp_hand.append(card)

                    #_cards.remove(card)

            if len(temp_hand) == 4:
                relevant_cards.extend(temp_hand)
            else:
                print('{0} does not make quads.', parent_card.toString())

        #at this point, relevant_cards has either 4 or 0 values

        if len(relevant_cards) == 3:
            #calculates remaining cards for use in determining high cards (XOR operation)
            remaining_cards = relevant_cards.difference(initial_cards)
            self.__best_hand = relevant_cards.extend(self.calculate_high_cards(remaining_cards, 1))
            return True

        else:
            return False


    def check_for_full_house(self, cards):



    def check_for_flush(self, cards):

        made_flush = []

        flush_s = []
        flush_d = []
        flush_c = []
        flush_h = []

        for card in cards :
            if(card.suit == 'H'):
                flush_h.append(card)
            elif(card.suit == 'S'):
                flush_s.append(card)
            elif(card.suit == 'C'):
                flush_c.append(card)
            elif(card.suit == 'D'):
                flush_d.append(card)
            else:
                raise Exception('This card does not have a valid suit.')

        if len(flush_h) >= 5 :
            made_flush = flush_h
        elif len(flush_c) >= 5 :
            made_flush = flush_c
        elif len(flush_d) >= 5 :
            made_flush = flush_d
        elif len(flush_s) >= 5 :
            made_flush = flush_s
        else :
            #the hand does not make a hand
            return []

        made_flush = self.calculate_high_cards(made_flush, 5)

        return made_flush


    def check_for_straight(self, cards):
        var = len(cards) - 1
        straight_counter = 0

        while var >= 0:
            if cards[var] - cards[var - 1] == 1:
                straight_counter += 1
            var -= 1

        if straight_counter == 5:
            return True
        else:
            return False

    def check_for_trips(self, cards):
        initial_cards = cards
        relevant_cards = []
        remaining_cards = []

        for parent_card in cards:
            temp_hand = [parent_card]

            for card in cards:
                if (parent_card.value == card.value) and (parent_card.suit != card.suit):
                    temp_hand.append(card)

                    #_cards.remove(card)

            if len(temp_hand) == 3:
                relevant_cards.extend(temp_hand)
            else:
                print('{0} does not make trips.', parent_card.toString())

        #at this point, relevant_cards has either 0 or 3 or 6 values

        if len(relevant_cards) == 3:
            #calculates remaining cards for use in determining high cards (XOR operation)
            remaining_cards = relevant_cards.difference(initial_cards)
            self.__best_hand = relevant_cards.extend(self.calculate_high_cards(remaining_cards, 2))
            return True

        elif len(relevant_cards) == 6:
            #handle 6 cards

        else:
            return False




    def check_for_two_pair(self, cards):



    def check_for_pair(self, cards):
        trips = []
        pairs = []
        quads = []

        for parent_card in cards:
            hand = [parent_card]

            for card in cards:
                if (parent_card.value == card.value) and (parent_card.suit != card.suit):
                    hand.append(card)

            if len(hand) == 2:
                pairs.append(tuple(hand))
            elif len(hand) == 3:
                trips.append(tuple(hand))
            elif len(hand) == 4:
                quads.append(tuple(hand))
            else:
                print('{0} does not make a paired hand.', parent_card.toString())

        if len(quads) > 0:
            remaining_cards =
            get_high_cards(remaining_cards, 1):

        if len(trips) > 0:








def calculate_hands(board, hands):
    made_hands = {
        'pair': 0,
        'two-pair': 0,
        'set': 0,
        'trips': 0,
        'open-ended': 0,
        'belly-buster': 0,
        'flush-draw': 0,
        'straight': 0,
        'full-house': 0,
        'quads': 0
    }

    return made_hands





        #_cards = cards

        #for parent_card in cards:
        #    temp_hand = [parent_card]

        #    for card in cards:
        #        if (parent_card.value == card.value) and (parent_card.suit != card.suit):
        #            temp_hand.append(card)
        #            _cards.remove(card)

        #    if len(temp_hand) == 4:
        #        made_hand = get_high_cards(hand, _cards)
        #        self.__best_hand = made_hand
        #        return True
        #    else:
        #        print('{0} does not make quads.', parent_card.toString())





    #def remove_low_cards(cards):
    #    trimmed_cards = cards
    #    while len(trimmed_cards) > 5 :
    #        previous = None
    #        lowest = None
    #        for card in trimmed_cards :
    #            if not previous or previous.
    #        trimmed_cards.delete(lowest)
    #
    #    return trimmed_cards

    #def get_high_cards(cards, number_of_high_cards):
    #    highest_cards = []
    #
    #    while len(highest_cards) < number_of_high_cards:
    #
    #
    #    return cards






        #straight = []
        #trips = []
        #two_pair = []


        #for(card in board_with_hand):
        #    if()

        #if(trips and two_pair):
        #    full_house = []

        #if(flush and straight):
        #    straight_flush = []


        #fill_high_cards()


        #check_for_straight_flush

        #check_for_pair


        #self.__best_hand = best_hand


        #merge board and hand into list
        #choose best 5-card hand from list




