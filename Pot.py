__author__ = 'Nick'

class Pot:

    def __init__(self):
        self.__pot = 0
        self.__contributions = {} #e.g. Player1: 15
        self.__actions = [] #ordered list of Action objects

    def getPot(self):
        return self.__pot

    def addToPot(self, player, amount):
        if not self.__contributions[player]:
            self.__contributions[player] = amount
        else:
            self.__contributions[player] += amount
        self.__pot += amount

    def getPlayerContribution(self, player):
        return self.__contributions[player] if self.__contributions[player] else 0
