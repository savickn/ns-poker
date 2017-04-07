__author__ = 'Nick'

import HandStraight, Helpers, Data

#can be passed any number of cards, set-based approach
def analyzeStraights(availableCards):
    straights = []
    straightOuts = []
    backdoorOuts = []

    oneOuters = []
    twoOuters = []
    backdoorOneOuters = []
    backdoorTwoOuters = []

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
            if out not in straightOuts:
                straightOuts.append(out)

        elif len(values & cardTypes) == 3:
            drawOuts = values - cardTypes
            for o in drawOuts:
                if o not in backdoorOuts:
                    backdoorOuts.append(o)

    print(straightOuts)
    print(backdoorOuts)


cards13 = [
    Data.six_spades,
    Data.seven_spades,
    Data.three_clubs,
    Data.four_diamonds,
    Data.five_hearts,
    Data.jack_spades]


analyzeStraights(cards13)
