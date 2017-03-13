__author__ = 'Nick'

import Avatar
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

#most classes show implement Interface Drawable for setSprite() and draw() commands
class Card:
    #unique id for each card
    __id = None

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
        #self.__id = '{value}-{suit}'.format(value=value, suit=suit)
        self.__type = type
        self.__suit = suit
        self.__high_value = value
        self.__low_value = options['low_value'] if options['low_value'] is not None else value

        self.checkRep()

    #def __eq__(self, other):
    #    return self.getId() == other.getId()

    def __lt__(self, other):
        return self.getHighValue() < other.getHighValue()

    def __gt__(self, other):
        return self.getHighValue() > other.getHighValue()

    def checkRep(self):
        assert self.__high_value in range(2, 15)
        #assert self.__low_value in [None, 1]
        assert self.__type in ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        assert self.__suit in ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        assert self.__hidden in [True, False]

    ########## SETTERS & GETTERS ############

    def getId(self):
        return self.__id

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

    ########### GRAPHICS ##########

    def draw(self):
        self.__sprite.draw()

    def setSprite(self):
        self.__sprite = Avatar.Avatar('/path/to/picture')

    ########## UTILITY ###########

    def toString(self):
        return '{type} of {suit}'.format(type = self.__type, suit = self.__suit)

