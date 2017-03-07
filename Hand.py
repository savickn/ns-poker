__author__ = 'Nick'

prefixes = {
    'Straight Flush': 'Z',
    'Quads': 'Q',
    'Full House': 'H',
    'Flush': 'F',
    'Straight': 'S',
    'Trips': 'T',
    'Two Pair': 'W',
    'Pair': 'P'
}

multipliers = {
    'Clubs': 1,
    'Diamonds': 2,
    'Hearts': 3,
    'Spades': 4
}

class Hand:
    __cards = None
    __value = None #e.g. highest card in flush,
    __length = None #length of hand (e.g. pair = 2, flush = 5)
    __identifier = None #unique for every possible hand

    def __init__(self, cards, value, length, prefix):
        self.__cards = list(cards)
        self.__value = value
        self.__length = length
        self.__identifier = self.setIdentifier(prefix)

    #used to check if a particular hand already exists in a collection
    def __eq__(self, other):
        if self.__identifier == other.getIdentifier():
            return True
        else:
            return False

    ########## GETTERS ###########

    def getCards(self):
        return self.__cards

    def getValue(self):
        return self.__value

    def getLength(self):
        return self.__length

    def getIdentifier(self):
        return self.__identifier

    ########### SETTERS ###########

    def setIdentifier(self, prefix):
        code = 0
        for card in self.__cards:
            code += multipliers[card.getSuit()] + card.getHighValue()
        return prefix + '-' + str(self.__value) + '-' + str(code)





