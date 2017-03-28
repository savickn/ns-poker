__author__ = 'Nick'

class Pot:

    def __init__(self):
        self.__pot = 0
        self.__contributions = {} #e.g. Player1: 15
        self.__actions = [] #ordered list of Action objects

    def getPot(self):
        return self.__pot

    def getPlayerContribution(self, player):
        return self.__contributions[player.getHash()]

    def registerActivePlayers(self, players):
        for player in players:
            self.__contributions[player.getHash()] = 0

    def handleAction(self, action):
        self.__contributions[action.getActor().getHash()] += action.getAmount()
        self.__actions.append(action)
        self.__pot += action.getAmount()
        self.printAsString()

    ################ UTILITY METHODS ##################

    def printAsString(self):
        print('Pot: {pot}'.format(pot=self.__pot))
        print('####### CONTRIBUTIONS ########')
        for key, value in self.__contributions:
            print('{player} has invested {amount}'.format(player=key, amount=value))
