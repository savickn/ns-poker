__author__ = 'Nick'


class Draw:

    def __init__(self, type, cards, outs):
        self.__type = type #must be a prefix
        self.__cards = cards #list of Card objects
        self.__outs = outs #list of Card objects that will create a MadeHand

        #self.__nut = None #will this hand make the nut-flush/straight, must be Boolean, probably not needed cuz can find the resulting BestHand in the ordered list of BestHands

    ############ SETTERS AND GETTERS ###########

    def getType(self):
        return self.__type

    def getCards(self):
        return self.__cards

    def getOuts(self):
        return self.__outs

    ############# UTILITY METHODS #############

    def checkRep(self):
        assert self.__type in ['Z', 'Q', 'B', 'F', 'S', 'T', 'W', 'P'] # made hands
        assert len(set(self.__cards) & set(self.__outs)) == 0
