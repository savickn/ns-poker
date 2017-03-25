__author__ = 'Nick'

class Pot:

    def __init__(self):
        self.__pot = 0
        self.__committedMoney = {
            'Player1': 15
        }

    def getMaxBet(self):
        return self.__pot
