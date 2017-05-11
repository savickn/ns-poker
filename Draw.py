__author__ = 'Nick'


class Draw:

    def __init__(self, type, cards, outs):
        self.__type = type #must be a prefix
        self.__cards = cards #list of Card objects
        self.__outs = outs #list of Card objects that will create a MadeHand

    def __str__(self):
        rep = None
        for c in self.getOuts():
            rep = c.toString() if rep is None else rep + ', {card}'.format(card=c.toString())
        return '# Outs: {cards} \n'.format(cards=rep)

    ############ SETTERS AND GETTERS ###########

    def getType(self):
        return self.__type

    def getCards(self):
        return self.__cards

    def getOuts(self):
        return self.__outs

    def countOuts(self):
        return len(self.__outs)

    ############# UTILITY METHODS #############

    def checkRep(self):
        assert self.__type in ['Z', 'Q', 'B', 'F', 'S', 'T', 'W', 'P'] # made hands
        assert len(set(self.__cards) & set(self.__outs)) == 0
