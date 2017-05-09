__author__ = 'Nick'

from itertools import cycle
import Data


hand = [
    Data.ace_hearts,
    Data.ace_spades,
    Data.king_spades,
    Data.eight_diamonds,
    Data.seven_clubs,
    Data.two_diamonds,
    Data.four_spades
]

for card in hand[1:6]:
    print(card.toString())

#licycle = cycle(li)
#nextelem = licycle.next()
#thiselem, nextelem = nextelem, licycle.next()

class CircleList:
    __items = []

    def __init__(self):
        print('init')

    def getItems(self):
        return self.__items

    def addItem(self, item):
        self.__items.append(item)

class CircleListItem:
    __card = None
    __previous = None
    __next = None

    def __init__(self, card, prev, next):
        __card = card
        __previous = prev
        __next = next


class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):
    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

#print(x.Name())
#print(y.GetEmployee())


def calculate_high_cards(relevant_cards, remaining_cards) :
    _relevant_cards = relevant_cards
    _remaining_cards = remaining_cards
    number_of_cards = len(relevant_cards) + len(remaining_cards)
    assert(number_of_cards > 4)

    _remaining_cards.sort(key=lambda card: card.getHighValue(), reverse=True)

    while len(_relevant_cards) < 5 :
        _relevant_cards.append(_remaining_cards.pop(0))

    assert len(_relevant_cards) == 5
    assert len(_remaining_cards) == number_of_cards - len(_relevant_cards)

    return _relevant_cards

def printAsString(self):
    print('### BEST HAND ###')
    print(self.__primary)
    print(self.__secondary)

    cards = self.__primary.getCards() + self.__secondary.getCards() if self.__secondary else self.__primary.getCards()
    for c in cards:
        print(c.toString())

    print('# HOLE CARDS #')
    for c in self.__startingHand.getCards():
        print(c.toString())



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

#returns true if two cards are within 1 value of each other
#def isConnected(card1, card2):
#    highDiff = abs(card1.getHighValue() - card2.getHighValue())
#    lowDiff = abs(card1.getLowValue() - card2.getLowValue())
#    return True if (highDiff == 1) or (lowDiff == 1) else False

#def getConnectionFactor(card1, card2):
#    highDiff = abs(card1.getHighValue() - card2.getHighValue())
#    lowDiff = abs(card1.getLowValue() - card2.getLowValue())
#    return highDiff if highDiff < lowDiff else lowDiff

