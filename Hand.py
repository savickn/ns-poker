__author__ = 'Nick'

prefixes = {
    'Straight Flush': 'Z',
    'Quads': 'Q',
    'Full House': 'B',
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
    __prefix = None #used for hand rankings
    __cards = None #collection of cards used to make the hand (up to 5 cards)
    __primaryValue = None #e.g. highest card in flush, value of a pair, etc
    __length = None #length of hand (e.g. pair = 2, flush = 5)
    __identifier = None #unique for every possible hand, mainly used to differentiate hands of the same ranking

    def __init__(self, cards, value, length, prefix):
        self.__cards = list(cards)
        self.__primaryValue = value
        self.__length = length
        self.__identifier = self.setIdentifier(prefix)

        self.checkRep()

    #used to check if a particular hand already exists in a collection
    def __eq__(self, other):
        if self.__identifier == other.getIdentifier():
            return True
        else:
            return False

    ########## GETTERS ###########

    def getCards(self):
        return self.__cards

    def getPrimaryValue(self):
        return self.__primaryValue

    def getLength(self):
        return self.__length

    def getIdentifier(self):
        return self.__identifier

    def getPrefix(self):
        return self.__prefix

    ############ SETTERS #############

    def setIdentifier(self, prefix):
        code = 0
        for card in self.__cards:
            code += multipliers[card.getSuit()] + card.getHighValue()
        return prefix + '-' + str(self.__primaryValue) + '-' + str(code)

    ############ UTILITY #############

    def toString(self):
        for card in self.__cards:
            print(card.toString())

    def checkRep(self):
        assert self.__identifier[0] == self.__prefix
        assert len(self.__cards) in [2, 3 ,4, 5]




