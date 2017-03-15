__author__ = 'Nick'

import Deck

#returns true if two cards are within 1 value of each other
def isConnected(card1, card2):
    primary_diff = abs(card1.getHighValue() - card2.getHighValue())
    secondary_diff = None
    #analyzing low values
    if(card1.getLowValue()):
        secondary_diff = abs(card1.getLowValue() - card2.getHighValue())
    if(card2.getLowValue()):
        secondary_diff = abs(card2.getLowValue() - card1.getHighValue())
    #final check, or (primary_diff == 0)
    if(primary_diff == 1) or (secondary_diff == 1):
        return True
    else:
        return False

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

#used to remove Pairs when checking for straights, careful it could remove both Pair cards
def removePairs(cards, suit):
    filtered = []
    for c in cards:
        if c.getSuit() == suit:
            filtered.append(c)
    for c in cards:
        if c in filtered:
            continue
        for c2 in filtered:
            if c.getHighValue() == c2.getHighValue():
                continue
        filtered.append(c)
    return filtered

#straight flush
board = [
    Deck.seven_spades,
    Deck.ten_hearts,
    Deck.jack_spades,
    Deck.jack_clubs,
    Deck.queen_diamonds,
    Deck.king_spades,
    Deck.ace_spades
]

suit = getRelevantSuit(board)
print(suit)
filteredCards = removePairs(board, suit)
for c in filteredCards:
    print(c.toString())


#uses 'isConnected' to check if all cards are connected
def isStraight(cards):
    suit = getRelevantSuit(cards)
    cards = removePairs(cards, suit)

    length = len(cards)
    c5c4 = isConnected(cards[length-1], cards[length-2])
    c4c3 = isConnected(cards[length-2], cards[length-3])
    c3c2 = isConnected(cards[length-3], cards[length-4])
    c2c1 = isConnected(cards[length-4], cards[length-5])
    if(c5c4 and c4c3 and c3c2 and c2c1):
        return True
    else:
        return False

#helper for checking if a collection of cards makes a flush
def isFlush(cards):
    suit = cards[0].getSuit()
    for c in cards:
        if c.getSuit() == suit:
            continue
        else:
            return False
    return True

def printCards(cards):
    for card in cards:
        print(card.toString())

#sorts based on a card's highValue field (highest value to lowest if reverse=True and vice versa)
def sortCards(cards, reverse):
    sorted_cards = sorted(cards, key=lambda card: card.getHighValue(), reverse=reverse)
    return sorted_cards

#sorts based on a card's lowValue field
def lowSort(cards, reverse):
    sorted_cards = sorted(cards, key=lambda card: card.getLowValue(), reverse=reverse)
    return sorted_cards

def inCollection(hand, collection):
    for h in collection:
        if h == hand:
            return True
    return False








#printCards(sortCards(hand, True))
#printCards(sortCards(hand, False))






#def getCollectionDiff(col1, col2):
#    diff = []
#    for c in col2:
#        if c not in col1:
#            diff.append(c)
#    return diff

#Helper function for analyzing all combinations of flushes
#def extractFlushes(self, cards):
#    cards.sort(key=lambda card: card.getHighValue(), reverse=True)
#    if len(cards) == 5:
#        self.__flushes.append(HandFlush.Flush(cards, cards[0].getHighValue()))
#    if len(cards) == 6:
#        self.__flushes.append(HandFlush.Flush(cards[:5], cards[0].getHighValue()))
#        self.__flushes.append(HandFlush.Flush(cards[1:6], cards[0].getHighValue()))
#    if len(cards) == 7:
#        self.__flushes.append(HandFlush.Flush(cards[:5], cards[0].getHighValue()))
#        self.__flushes.append(HandFlush.Flush(cards[1:6], cards[0].getHighValue()))
#        self.__flushes.append(HandFlush.Flush(cards[2:7], cards[0].getHighValue()))

#fills a given hand with high cards and returns the resulting 5 card hand... working
#def calculateHighCards(relevant_cards, remaining_cards) :
#    _relevant_cards = relevant_cards
#    _remaining_cards = remaining_cards
#    number_of_cards = len(relevant_cards) + len(remaining_cards)
#    assert(number_of_cards > 4)

#    _remaining_cards.sort(key=lambda card: card.getHighValue(), reverse=True)

#    while len(_relevant_cards) < 5 :
#        _relevant_cards.append(_remaining_cards.pop(0))

#    assert len(_relevant_cards) == 5
#    assert len(_remaining_cards) == number_of_cards - len(_relevant_cards)

#    return _relevant_cards


#accepts 2 'bestHand' arrays and returns the winner (or returns 'split pot' if 2 or more players tied)
#@staticmethod
#def compareHands(hand1, hand2):
#    for x, y in hand1, hand2:
#        if handRankings[x.getPrefix()] > handRankings[y.getPrefix()]:
#            print('WINNER: {hand}'.format())
#            return hand1
#        elif handRankings[y.getPrefix()] > handRankings[x.getPrefix()]:
#            return hand2
#        elif handRankings[x.getPrefix()] == handRankings[y.getPrefix()]:
#            winner = x.compare(y)
#            if winner is not None:
#                return winner
#        else:
#            raise Exception('One or more hand prefixes is not valid.')
#    return 'Split Pot' #returns if both players hands are identical
