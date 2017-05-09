__author__ = 'Nick'

import HandStraight, Data
from Helpers import GeneralHelpers, StraightHelpers

from collections import deque

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

    suit = StraightHelpers.getRelevantSuit(availableCards)
    cards = StraightHelpers.removePairs(availableCards, suit) #used to remove Pairs which interfere in Straight calculations
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



####################### ALTERNATIVE APPROACHES #########################


#should be passed a List of 5-card slices, connection-based approach
def analyzeStraightsByConnection(cards):
    assert len(cards) in range(5, 8)
    sorted_cards = deque(GeneralHelpers.highSort(cards, False))
    list_length = len(sorted_cards)

    relevant_cards = []

    it = 0
    while it < list_length:
        if StraightHelpers.isConnectedCollection(sorted_cards):
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


#should be passed a List of 5-card slices, pattern-based approach
def analyzeStraightsByPattern(cards):
    straights = []
    gutters = []
    doubleGutters = []
    openEnders = []

    suit = StraightHelpers.getRelevantSuit(cards)
    cards = StraightHelpers.removePairs(cards, suit) #used to remove Pairs which interfere in Straight calculations

    if len(cards) < 5:
        return

    low = GeneralHelpers.lowSort(cards, False)
    high = GeneralHelpers.highSort(cards, False)

    highPattern = StraightHelpers.extractPattern(high)
    lowPattern = StraightHelpers.extractPattern(low)

    pattern = None

    if '111' in highPattern:
        print('open ender')
    elif pattern == '121':
        print('gutter')
    elif pattern == '2112':
        print('double gutter')
    elif pattern == '1111':
        print('straight')
