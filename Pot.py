__author__ = 'Nick'

import ActionCall, ActionCheck, ActionRaise

class Pot:

    def __init__(self, bb):
        self.__pot = 0
        self.__bbStake = bb
        self.__contributions = {} #e.g. Player1: 15
        self.__actions = [] #ordered list of Action objects

    ############ GETTERS AND SETTERS ############

    def getPot(self):
        return self.__pot

    def getHighestContribution(self):
        high = 0
        for key, value in self.__contributions.items():
            if value > high:
                high = value
        return high

    def getPlayerContribution(self, player):
        return self.__contributions[player.getHash()]

    def getPublicState(self, player):
        state = {
            'pot': self.getPot(),
            'currentBet': self.getHighestContribution(),
            'playerContribution': self.getPlayerContribution(player)
        }
        minRaise = 2*(state['currentBet'] - state['playerContribution'])
        state['minRaise'] = minRaise if minRaise > 0 else self.__bbStake
        return state

    ############ ACTIONS AND BETTING #############

    def hasActed(self, player, street):
        actions = self.__actions[street]
        for action in actions:
            if action.getActor() == player and isinstance(action, (ActionCall.Call, ActionRaise.Raise, ActionCheck.Check)):
                return True
        return False

    def registerActivePlayers(self, players):
        for player in players:
            self.__contributions[player.getHash()] = 0

    def handleAction(self, action):
        amount = action.getAmount()
        self.__contributions[action.getActor().getHash()] += amount
        self.__actions.append(action)
        self.__pot += amount
        #if amount > self.__lastBet:
        #    self.__lastBet = amount
        self.printAsString()

    ################ UTILITY METHODS ##################

    def printAsString(self):
        print('####### CONTRIBUTIONS ########')
        print(self.__contributions)
        print('Pot: {pot}'.format(pot=self.__pot))
        #for key, value in self.__contributions:
        #    print('{player} has invested {amount}'.format(player=key, amount=value))
