__author__ = 'Nick'

import HandStraight, Helpers, Data
from collections import deque

from Helpers import Helpers, GeneralHelpers, StraightHelpers

simple_straight = [
    Data.king_spades,
    Data.queen_clubs,
    Data.jack_spades,
    Data.ten_spades,
    Data.ace_hearts,
]

complex_straight = [
    Data.ace_hearts,
    Data.four_spades,
    Data.five_clubs,
    Data.three_spades,
    Data.two_spades
]

multi_straight = [
    Data.eight_clubs,
    Data.seven_spades,
    Data.queen_clubs,
    Data.jack_spades,
    Data.ten_spades,
    Data.nine_diamonds,
    Data.six_hearts
]

straight_draw = [
    Data.ace_clubs,
    Data.three_clubs,
    Data.five_spades,
    Data.king_hearts,
    Data.queen_diamonds,
    Data.jack_clubs
]


#can be passed any number of cards, set-based approach
def analyzeStraights(availableCards):
    straights = []
    straightOuts = []
    backdoorOuts = []

    suit = Helpers.getRelevantSuit(availableCards)
    cards = Helpers.removePairs(availableCards, suit) #used to remove Pairs which interfere in Straight calculations
    cardTypes = {c.getType() for c in cards}

    for k, v in Data.straights.items():
        values = {c.getType() for c in v.getCards()}
        if len(values & cardTypes) == 5:
            straightCards = [c for c in cards if c.getType() in values]
            straight = HandStraight.Straight(straightCards, v.getPrimaryValue())

            #ensures no duplicate straights are added
            if not GeneralHelpers.inCollection(straight, straights):
                straights.append(straight)

        elif len(values & cardTypes) == 4:
            out = values - cardTypes
            for o in out:
                if o not in straightOuts:
                    straightOuts.append(o)
                    if o in backdoorOuts:
                        backdoorOuts.remove(o)

        elif len(values & cardTypes) == 3:
            drawOuts = values - cardTypes
            for o in drawOuts:
                if o not in backdoorOuts and o not in straightOuts:
                    backdoorOuts.append(o)

    print(straights)
    print(straightOuts)
    print(backdoorOuts)



analyzeStraights(simple_straight)
analyzeStraights(complex_straight)
analyzeStraights(multi_straight)
analyzeStraights(straight_draw)




def check_for_straight(cards):
    assert len(cards) in range(5, 8)
    sorted_cards = deque(sort_cards(cards, False))
    list_length = len(sorted_cards)

    relevant_cards = []

    it = 0
    while it < list_length:
        if isConnectedCollection(sorted_cards):
            straight = list(sorted_cards)
            relevant_cards = straight[-5:]
            break
        else:
            sorted_cards.rotate(1)
            it += 1

    for card in relevant_cards:
        print(card.toString())

    if len(relevant_cards) == 5:
        return True
    else:
        return False
