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

initials = {
    'Ace': 'A',
    'King': 'K',
    'Queen': 'Q',
    'Jack': 'J',
    'Ten': 'T',
    'Nine': '9',
    'Eight': '8',
    'Seven': '7',
    'Six': '6',
    'Five': '5',
    'Four': '4',
    'Three': '3',
    'Two': '2'
}


defaultOptions = {
    'low_value': None
}

#most classes show implement Interface Drawable for setSprite() and draw() commands
class Card:
    #unique id for each card
    __id = None

    __sprite = None

    def __init__(self, type, suit, value, options=defaultOptions):
        #self.__id = '{value}-{suit}'.format(value=value, suit=suit)
        self.__type = type
        self.__suit = suit
        self.__high_value = value
        self.__low_value = options['low_value'] if options['low_value'] is not None else value

        self.__hidden = True #used to determine if card should be drawn face-up or face-down

        self.checkRep()

    #used to check if two Cards are identical (e.g. Js == Js but Jh != Js), not working
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
        assert isinstance(self.__hidden, bool)

    ########## SETTERS & GETTERS ############

    #def getId(self):
    #    return self.__id

    def getInitial(self):
        return initials[self.__type]

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

