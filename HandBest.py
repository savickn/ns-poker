__author__ = 'Nick'

import Hand

handRankings = {
    'Z': 9,
    'Q': 8,
    'B': 7,
    'F': 6,
    'S': 5,
    'T': 4,
    'W': 3,
    'P': 2,
    'C': 1
}

class HandBest:
    __primary = None #of type Hand
    __secondary = None #of type Hand

    def __init__(self, primary, secondary=None):
        self.__primary = primary
        self.__secondary = secondary
        self.checkRep()

    #accepts a list of Cards and determines if they are contained with '__primary' and '__secondary'
    def __contains__(self, cards):
        bestCards = self.__primary.getCards() + self.__secondary.getCards()
        matchedCards = []
        for c1 in cards:
            if c1 in bestCards:
                matchedCards.append(c1)
            else:
                return False
        if matchedCards == cards:
            return True

    #helper function for 'compare'
    def analyzePrefix(self, p1, p2):
        if p1 > p2:
            return True
        elif p2 > p1:
            return False
        elif p1 == p2:
            return None

    #used to compare 2 HandBest objects and return the winner
    def compare(self, other):
        case1 = self.analyzePrefix(self.getPrimary().getPrefix(), other.getPrimary().getPrefix())
        if case1 is True:
            return self
        elif case1 is False:
            return other
        else:
            winner = self.getPrimary().compare(other.getPrimary())
            if winner is not None:
                return winner
            else:
                case2 = self.analyzePrefix(self.getSecondary().getPrefix(), other.getSecondary().getPrefix())
                if case2 == True:
                    return self
                elif case2 == False:
                    return other
                else:
                    winner = self.getSecondary().compare(other.getSecondary())
                    w = winner if not None else 'Split Pot'
                    return w

    ############# SETTERS AND GETTERS #############

    def getPrimary(self):
        return self.__primary

    def getSecondary(self):
        return self.__secondary

    ############# UTILITY METHODS #############

    def printAsString(self):
        cards = self.__primary.getCards() + self.__secondary.getCards() if self.__secondary else self.__primary.getCards()
        for c in cards:
            print(c.toString())

    def checkRep(self):
        assert isinstance(self.__primary, Hand.Hand)
        if self.__secondary:
            assert isinstance(self.getSecondary(), Hand.Hand)

