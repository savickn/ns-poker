__author__ = 'Nick'


import HandStraight

from Helpers import Helpers


#can be passed any number of cards, set-based approach
def analyzeStraights(availableCards):
    straights = []
    straightOuts = []
    backdoorOuts = []

    oneOuters = []
    twoOuters = []
    backdoorOneOuters = []
    backdoorTwoOuters = []

    suit = getRelevantSuit(availableCards)
    cards = removePairs(availableCards, suit) #used to remove Pairs which interfere in Straight calculations
    cardTypes = {c.getType() for c in cards}
    print(cardTypes)

    for key, values in Data.straights.items():
        if len(values & cardTypes) == 5:
            value = int(key[0])
            straightCards = [c for c in cards if c.getType() in values]
            straight = HandStraight.Straight(straightCards, value)

            #ensures no duplicate straights are added
            if not inCollection(straight, straights):
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

#must be passed 5 sorted cards, WORKING
def isStraight(cards):
    assert len(cards) == 5
    return True if(cards[4].getHighValue() - cards[0].getHighValue() == 4) or (cards[4].getLowValue() - cards[0].getLowValue() == 4) else False

#returns the smallest gap between two cards
def getConnectionFactor(card1, card2):
    high = abs(card1.getHighValue() - card2.getHighValue())
    low = abs(card1.getLowValue() - card2.getLowValue())
    return high if high < low else low

#returns true if two cards are within 1 value of each other
def isConnected(card1, card2):
    return True if getConnectionFactor(card1, card2) == 1 else False

#returns True if isConnected returns True for all cards, pretty bad code
def isConnectedCollection(cards):
    length = len(cards)
    c5c4 = isConnected(cards[length-1], cards[length-2])
    c4c3 = isConnected(cards[length-2], cards[length-3])
    c3c2 = isConnected(cards[length-3], cards[length-4])
    c2c1 = isConnected(cards[length-4], cards[length-5])
    return True if (c5c4 and c4c3 and c3c2 and c2c1) else False


############# MEMORY APPROACH ##############




############## CONNECTION APPROACH ###############



############# PATTERN APPROACH ##############

#used to analyze the pattern of gaps between cards in a hand
def extractPattern(cards):
    pattern = ''
    for x in range(len(cards)):
        try:
            value = getConnectionFactor(cards[x+1], cards[x])
            pattern += str(value)
        except IndexError:
            break
    return pattern

#should be passed a List of 5-card slices, pattern-based approach
def analyzeStraightPatterns(cards):
    straights = []
    gutters = []
    doubleGutters = []
    openEnders = []

    suit = getRelevantSuit(cards)
    cards = removePairs(cards, suit) #used to remove Pairs which interfere in Straight calculations

    if len(cards) < 5:
        return

    low = lowSort(cards, False)
    high = highSort(cards, False)

    highPattern = extractPattern(high)
    lowPattern = extractPattern(low)

    pattern = None

    if '111' in highPattern:
        print('open ender')
    elif pattern == '121':
        print('gutter')
    elif pattern == '2112':
        print('double gutter')
    elif pattern == '1111':
        print('straight')
