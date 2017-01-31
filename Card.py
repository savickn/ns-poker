__author__ = 'Nick'

from PokerCalculator import Avatar
from enum import Enum

card_values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14
}

class Card_Type(Enum):
    ACE_LO = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE_HIGH = 14

class Card_Suit(Enum):
    CLUBS = 1
    HEARTS = 2
    DIAMONDS = 3
    SPADES = 4

#most classes show implement Interface Drawable for setSprite() and draw() commands
class Card:
    #should be enum Card_Type
    __type = None

    #should be enum Card_Suit
    __suit = None

    #used to represent card value (e.g. Queen = 12, King = 13, Ace = 14)
    __high_value = None

    #used to represent a value of 1 for Aces
    __low_value = None

    #used to determine if card should be shown or not
    __hidden = True

    __sprite = None

    def __init__(self, type, suit, value, options={'low_value':None}):
        self.__type = type
        self.__suit = suit
        self.__high_value = value
        self.__low_value = options['low_value']

        self.checkRep()

    def __lt__(self, other):
        return self.getHighValue() < other.getHighValue()

    def __gt__(self, other):
        return self.getHighValue() > other.getHighValue()

    def checkRep(self):
        assert self.__high_value in range(2, 15)
        assert self.__low_value in [None, 1]
        assert self.__type in ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        assert self.__suit in ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        assert self.__hidden in [True, False]

    ########## SETTERS & GETTERS ############

    def getHighValue(self):
        return self.__high_value

    def getLowValue(self):
        return self.__low_value

    def getType(self):
        return self.__type

    def getSuit(self):
        return self.__suit

    def getState(self):
        return self.__hidden

    def setState(self, state):
        assert state in [True, False]
        self.__hidden = state

    def setSprite(self):
        self.__sprite = Avatar.Avatar('/path/to/picture')

    ########### GRAPHICS ##########

    def draw(self):
        self.__sprite.draw()

    ########## UTILITY ###########

    def toString(self):
        return '{type} of {suit}'.format(type = self.__type, suit = self.__suit)

    def printAsString(self):
        print(self.toString())


    #@staticmethod
    #def compare(card1, card2):
    #    if card1.__primary_value > card2.__primary_value:
    #        return card1
    #    elif card1.__primary_value < card2.__primary_value:
    #        return card2
    #    else:
    #        return None
