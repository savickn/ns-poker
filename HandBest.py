__author__ = 'Nick'

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
    __primary = None
    __secondary = None

    def __init__(self, primary, secondary=None):
        self.__primary = primary
        self.__secondary = secondary

    #helper function for 'compare'
    def analyzePrefix(self, p1, p2):
        if p1 > p2:
            return True
        elif p2 > p1:
            return False
        elif p1 == p2:
            return None

    #finish this!!
    def compare(self, other):
        case1 = self.analyzePrefix(self.getPrimary().getPrefix(), other.getPrimary().getPrefix())
        if case1 is True:
            return self
        elif case1 is False:
            return other
        elif case1 is None:
            pr
        else:
            case2 = self.analyzePrefix(self.getSecondary().getPrefix(), other.getSecondary().getPrefix())
            if case2 == True:
                return self
            elif case2 == False:
                return other
            else:
                return 'Split Pot'

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
