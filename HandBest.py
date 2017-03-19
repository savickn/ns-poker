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
    __draws = None #of type Draw (must improve BestHand)

    def __init__(self, primary, secondary=None):
        self.__primary = primary
        self.__secondary = secondary
        self.checkRep()

    #accepts a list of Cards and determines if they are contained with '__primary' and '__secondary'
    def __contains__(self, cards):
        bestCards = self.__primary.getCards() + self.__secondary.getCards() if self.__secondary else self.__primary.getCards()
        for c1 in cards:
            if c1 in bestCards:
                return True
        return False

    #helper function for 'compare'
    def analyzePrefix(self, p1, p2):
        if p1 > p2:
            return True
        elif p2 > p1:
            return False
        elif p1 == p2:
            return None

    def __lt__(self, other):
        case1 = self.analyzePrefix(self.getPrimary().getPrefix(), other.getPrimary().getPrefix())
        if case1 is True:
            return -1
        elif case1 is False:
            return 1
        else:
            winner = self.getPrimary().compare(other.getPrimary()) #compares primary Hands with the same prefix
            if winner is True:
                return -1
            elif winner is False:
                return 1
            else:
                case2 = self.analyzePrefix(self.getSecondary().getPrefix(), other.getSecondary().getPrefix())
                if case2 == True:
                    return -1
                elif case2 == False:
                    return 1
                else:
                    winner = self.getSecondary().compare(other.getSecondary()) #compares secondary Hands with same prefix if necessary
                    if winner is True:
                        return -1
                    elif winner is False:
                        return 1
                    else:
                        return 0

    #used to compare 2 HandBest objects and pick the winner,
    @staticmethod
    def compare(self, other):
        case1 = self.analyzePrefix(self.getPrimary().getPrefix(), other.getPrimary().getPrefix())
        if case1 is True:
            return 1
        elif case1 is False:
            return -1
        else:
            winner = self.getPrimary().compare(other.getPrimary()) #compares primary Hands with the same prefix
            if winner is True:
                return 1
            elif winner is False:
                return -1
            else:
                case2 = self.analyzePrefix(self.getSecondary().getPrefix(), other.getSecondary().getPrefix())
                if case2 == True:
                    return 1
                elif case2 == False:
                    return -1
                else:
                    winner = self.getSecondary().compare(other.getSecondary()) #compares secondary Hands with same prefix if necessary
                    if winner is True:
                        return 1
                    elif winner is False:
                        return -1
                    else:
                        return 0

    ############# SETTERS AND GETTERS #############

    def getPrimary(self):
        return self.__primary

    def getSecondary(self):
        return self.__secondary

    def addDraw(self, draw):
        if handRankings[draw.getType()] >= handRankings[self.__primary.getPrefix()]:
            self.__draws.append(draw)

    ############# UTILITY METHODS #############

    def printAsString(self):
        print('### BEST HAND ###')
        print(self.__primary)
        print(self.__secondary)

        cards = self.__primary.getCards() + self.__secondary.getCards() if self.__secondary else self.__primary.getCards()
        for c in cards:
            print(c.toString())

    def checkRep(self):
        assert isinstance(self.__primary, Hand.Hand)
        if self.__secondary:
            assert isinstance(self.getSecondary(), Hand.Hand)
        assert (len(self.__primary.getCards()) == 5) or (len(self.__primary.getCards()) + len(self.__secondary.getCards()) == 5)

