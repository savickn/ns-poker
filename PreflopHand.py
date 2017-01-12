__author__ = 'Nick'


class HoldemHand:
    __card1 = None
    __card2 = None

    def __init__(self, card1, card2):
        self.__card1 = card1
        self.__card2 = card2

    def toString(self):
        return self.__card1.toString() + ', ' + self.__card2.toString()

    def printAsString(self):
        print(self.toString())

    def draw(self):
        self.__card1.draw()
        self.__card2.draw()

class OmahaHand:
    __card1 = None
    __card2 = None
    __card3 = None
    __card4 = None

    def __init__(self, card1, card2):
        self.__card1 = card1
        self.__card2 = card2

    def toString(self):
        return self.__card1.toString() + ', ' + self.__card2.toString()

    def printAsString(self):
        print(self.toString())

    def draw(self):
        self.__card1.draw()
        self.__card2.draw()


class StudHand:
    __card1 = None
    __card2 = None
    __card3 = None
    __card4 = None

    def __init__(self, card1, card2):
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


