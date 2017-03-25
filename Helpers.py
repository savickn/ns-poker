__author__ = 'Nick'


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

#must be passed 5 sorted cards, WORKING
def isStraight(cards):
    assert len(cards) == 5
    return True if(cards[4].getHighValue() - cards[0].getHighValue() == 4) or (cards[4].getLowValue() - cards[0].getLowValue() == 4) else False


def getStraightOuts(cards):


def isGutShotDraw():


def isOpenEndedDraw():



#helper for checking if a collection of cards makes a flush
def isFlush(cards):
    suit = cards[0].getSuit()
    for c in cards:
        if c.getSuit() == suit:
            continue
        else:
            return False
    return True

#sorts based on a card's highValue field (highest value to lowest if reverse=True and vice versa), WORKING
def highSort(cards, reverse):
    sorted_cards = sorted(cards, key=lambda card: card.getHighValue(), reverse=reverse)
    return sorted_cards

#sorts based on a card's lowValue field, WORKING
def lowSort(cards, reverse):
    sorted_cards = sorted(cards, key=lambda card: card.getLowValue(), reverse=reverse)
    return sorted_cards

#checks if a Hand (e.g. HandQuads or HandFlush) is in a collection (based on Hand.__id), WORKING
def inCollection(hand, collection):
    for h in collection:
        if h == hand:
            return True
    return False

def printCards(cards):
    for card in cards:
        print(card.toString())

#used to sort BestHand objects, not working
def sortBestHands(hands):
    sortedHands = sorted(hands, key=lambda hand: hand.getPrimary(), reverse=True)
    return sortedHands


import Board, Data

#Ace-high straight
board10 = Board.Board(
    Data.king_spades,
    Data.ace_clubs,
    Data.queen_diamonds,
    Data.ten_hearts,
    Data.jack_spades)

#Ace-low straight
board11 = Board.Board(
    Data.two_spades,
    Data.three_clubs,
    Data.four_diamonds,
    Data.five_hearts,
    Data.jack_spades)

#straight with A-high
board12 = Board.Board(
    Data.six_spades,
    Data.three_clubs,
    Data.four_diamonds,
    Data.five_hearts,
    Data.jack_spades)







#printCards(highSort(board10.getCards(), True))
#printCards(lowSort(board10.getCards(), True))






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

#
# #must be passed 5 sorted cards
# def isStraightOpt(cards):
#     assert len(cards) == 5
#     #print(cards)
#     highValues = []
#     lowValues = []
#     for c in cards:
#         highValues.append(c.getHighValue())
#         lowValues.append(c.getLowValue())
#
#     highValues.sort()
#     lowValues.sort()
#
#     if(abs(cards[4].getHighValue() - cards[0].get) == 4) or (abs(lowValues[4] - lowValues[0]) == 4):
#         return True
#

#uses 'isConnected' to check if all cards are connected
# def isStraightAlt(cards):
#     length = len(cards)
#     c5c4 = isConnected(cards[length-1], cards[length-2])
#     c4c3 = isConnected(cards[length-2], cards[length-3])
#     c3c2 = isConnected(cards[length-3], cards[length-4])
#     c2c1 = isConnected(cards[length-4], cards[length-5])
#     if(c5c4 and c4c3 and c3c2 and c2c1):
#         return True
#     else:
#         return False

#returns true if two cards are within 1 value of each other
# def isConnected(card1, card2):
#     primary_diff = abs(card1.getHighValue() - card2.getHighValue())
#     secondary_diff = None
#     #analyzing low values
#     if(card1.getLowValue()):
#         secondary_diff = abs(card1.getLowValue() - card2.getHighValue())
#     if(card2.getLowValue()):
#         secondary_diff = abs(card2.getLowValue() - card1.getHighValue())
#     #final check, or (primary_diff == 0)
#     if(primary_diff == 1) or (secondary_diff == 1):
#         return True
#     else:
#         return False