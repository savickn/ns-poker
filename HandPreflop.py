__author__ = 'Nick'

class PreflopHand:
    def __init__(self):
        x = 1

class HoldemHand(PreflopHand):
    __card1 = None
    __card2 = None

    def __init__(self, card1, card2):
        PreflopHand.__init__(self)
        self.__card1 = card1
        self.__card2 = card2

    def getCards(self):
        cards = [self.__card1, self.__card2]
        return cards

    def isSuited(self):
        if self.__card1.getSuit() == self.__card2.getSuit():
            return True
        else:
            return False

    def isPaired(self):
        if self.__card1.getHighValue() == self.__card2.getHighValue():
            return True
        else:
            return False

    def toString(self):
        return 'Holdem Hand: {card1}, {card2}'.format(card1=self.__card1.toString(), card2=self.__card2.toString())

    def draw(self):
        self.__card1.draw()
        self.__card2.draw()

class OmahaHand(PreflopHand):
    __card1 = None
    __card2 = None
    __card3 = None
    __card4 = None

    def __init__(self, card1, card2, card3, card4):
        PreflopHand.__init__(self)
        self.__card1 = card1
        self.__card2 = card2
        self.__card3 = card3
        self.__card4 = card4

    def toString(self):
        return self.__card1.toString() + ', ' + \
               self.__card2.toString() + ', ' + \
               self.__card3.toString() + ', ' + \
               self.__card4.toString()

    def printAsString(self):
        print(self.toString())

    def draw(self):
        self.__card1.draw()
        self.__card2.draw()
        self.__card3.draw()
        self.__card4.draw()


class StudHand(PreflopHand):
    __card1 = None
    __card2 = None
    __card3 = None
    __card4 = None

    def __init__(self, card1, card2):
        PreflopHand.__init__(self)
        self.__card1 = card1
        self.__card2 = card2

    def toString(self):
        return self.__card1.toString() + ', ' + self.__card2.toString()

    def printAsString(self):
        print(self.toString())

    def draw(self):
        self.__card1.draw()
        self.__card2.draw()

#class SuitedHand:


#class PairedHand:


