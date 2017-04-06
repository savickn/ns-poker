__author__ = 'Nick'

class PreflopHand:
    def __init__(self):
        x = 1

class HoldemHand(PreflopHand):

    def __init__(self, cards):
        PreflopHand.__init__(self)
        cards.sort(key=lambda card: card.getHighValue(), reverse=True)
        self.__card1 = cards[0]
        self.__card2 = cards[1]

    def __str__(self):
        return 'Holdem Hand: {card1}, {card2}'.format(card1=self.__card1, card2=self.__card2)

    ########### GETTERS ############

    def getCards(self):
        cards = [self.__card1, self.__card2]
        return cards

    def getInitials(self):
        str = self.__card1.getInitial() + self.__card2.getInitial()
        str += 's' if self.isSuited() else 'o'
        return str

    def isSuited(self):
        return True if self.__card1.getSuit() == self.__card2.getSuit() else False

    def isPaired(self):
        return True if self.__card1.getHighValue() == self.__card2.getHighValue() else False

    ############# GRAPHICS ###########

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


