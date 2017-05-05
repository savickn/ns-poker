__author__ = 'Nick'

import HandStraight, Helpers, Data

#can be passed any number of cards, set-based approach
def analyzeStraights(availableCards):
    straights = []
    straightOuts = []
    backdoorOuts = []

    suit = Helpers.getRelevantSuit(availableCards)
    cards = Helpers.removePairs(availableCards, suit) #used to remove Pairs which interfere in Straight calculations
    cardTypes = {c.getType() for c in cards}

    for key, values in Data.straights.items():
        if len(values & cardTypes) == 5:
            value = int(key[0])
            straightCards = [c for c in cards if c.getType() in values]
            straight = HandStraight.Straight(straightCards, value)

            #ensures no duplicate straights are added
            if not Helpers.inCollection(straight, straights):
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

cards13 = [
    Data.ace_spades,
    Data.five_spades,
    Data.three_clubs,
    Data.queen_clubs,
    Data.king_hearts,
    Data.jack_spades]


analyzeStraights(cards13)
