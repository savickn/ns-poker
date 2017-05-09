__author__ = 'Nick'


################## GENERAL METHODS ####################

#returns the most common suit in a collection of cards (relies on the fact that only only flush can be made at a time)
#can be used to remove irrelevant pair cards when checking for straights and straight flushes
def getRelevantSuit(cards):
    spades = 0
    clubs = 0
    hearts = 0
    diamonds = 0

    for card in cards:
        if card.getSuit() == 'Spades':
            spades += 1
        elif card.getSuit() == 'Diamonds':
            diamonds += 1
        elif card.getSuit() == 'Hearts':
            hearts += 1
        elif card.getSuit() == 'Clubs':
            clubs += 1
        else:
            raise Exception('This card has an invalid suit.')

    if (spades >= hearts) and (spades >= clubs) and (spades >= diamonds):
        return 'Spades'
    elif (clubs >= hearts) and (clubs >= spades) and (clubs >= diamonds):
        return 'Clubs'
    elif (hearts >= clubs) and (hearts >= spades) and (hearts >= diamonds):
        return 'Hearts'
    else:
        return 'Diamonds'


#used to remove Pairs before checking for straights
def removePairs(cards, suit):
    filtered = []
    #adds cards of relevant suit to the filtered cards
    for c in cards:
        if c.getSuit() == suit:
            filtered.append(c)
    for c in cards:
        if c in filtered: #skips suited cards
            continue
        isPaired = False
        for c2 in filtered:
            if c.getHighValue() == c2.getHighValue():
                isPaired = True
                break
        if not isPaired:
            filtered.append(c)
    return filtered


############# MEMORY APPROACH ##############




############## CONNECTION APPROACH ###############


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


#must be passed 5 sorted cards, WORKING
def isStraight(cards):
    assert len(cards) == 5
    return True if(cards[4].getHighValue() - cards[0].getHighValue() == 4) or (cards[4].getLowValue() - cards[0].getLowValue() == 4) else False

#works for unordered collections
def isStraight2(cards):
    highDist = max([c.getHighValue() for c in cards]) - min([c.getHighValue() for c in cards])
    lowDist = max([c.getLowValue() for c in cards]) - min([c.getLowValue() for c in cards])
    return True if highDist == 1 or lowDist == 1 else False


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

