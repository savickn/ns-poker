__author__ = 'Nick'


class HandAnalyzer:
    __available_cards = None
    __best_hand = None

    __straight_flush = False
    __quads = False
    __full_house = False
    __flush = False
    __straight = False
    __trips = False
    __two_pair = False
    __pair = False
    __nothing = True

    __flush_draw = False
    __gutshot_draw = False
    __open_ended_draw = False
    __backdoor_gutshot_draw = False
    __backdoor_open_ended_draw = False
    __backdoor_flush_draw = False

    def __init__(self, cards):
        if len(cards) > 7 or len(cards) < 5:
            raise Exception('HandAnalyzer failed to init')

        self.__available_cards = cards

    def get_best_hand(self):
        return self.__best_hand

    def calculate_best_hand(self, *input_cards):
        if input_cards:
            cards = input_cards
        else:
            cards = self.__available_cards

        #used to sort hand by value
        sorted_cards = cards.sort(key=lambda card: card.value)

        if self.check_for_straight_flush(sorted_cards):
            return self.__best_hand

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




