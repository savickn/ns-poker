__author__ = 'Nick'


class Draw:

    def __init__(self, type, cards, outs):
        self.__type = type #must be a prefix
        self.__cards = cards #list of Card objects
        self.__outs = None #cards that will improve this hand
        self.__nut = None #will this hand make the nut-flush/straight, must be Boolean




    def checkRep(self):
        assert self.__type in ['Z', 'Q', 'B', 'F', 'S', 'T', 'W', 'P']
