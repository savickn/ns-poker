__author__ = 'Nick'

from random import *
import ActionCall, ActionCheck, ActionFold, ActionRaise, ActionPostAnte, ActionPostSB, ActionPostBB

states = [
    'In Hand', #used for postflop play, e.g. player can BET/CHECK
    'Folded', # used for postflop play, e.g. player can no longer BET/CHECK
    'All In', #will be analyzed after RIVER but will not be given a chance to BET/CHECK
    'Active', #used for preflop play, will be dealt and hand and given a chance to CALL/RAISE the BB
    'Sitting Out' #used for preflop play, will not be dealt a hand
]

defaultOptions = {
    'UTG': [],
    'CO': [],
    'BTN': [],
    'SB': [],
    'BB': []
}

class Player:

    def __init__(self, account, buyin, **options):
        self.__account = account
        self.__hash = account + ''.join(["%s" % randint(0, 9) for num in range(9)])
        self.__stack = buyin #alternatively used 'account.withdraw(buyin)'
        self.__status = 'Active' #must be in [ACTIVE, SITTING_OUT]
        self.__hand = None #can be an Omaha or Texas Holdem hand

        self.__timeBank = None
        self.__tableView = None #must be initialized when Player joins using Game.getPublicInfo

        #self.__utgRange = options['UTG'] if options['UTG'] else []
        #self.__coRange = options['CO'] if options['CO'] else []
        #self.__btnRange = options['BTN'] if options['BTN'] else []
        #self.__sbRange = options['SB'] if options['SB'] else []
        #self.__bbRange = options['BB'] if options['BB'] else []

    def __str__(self):
        return '########## PLAYER ########## \n' \
               'Name: {name} \n' \
               'Stack: {stack} \n' \
               'Status: {status}'.format(name=self.__account, stack=self.__stack, status=self.__status)

    ############ Helper Methods ##############

    #for preflop play
    def isActive(self):
        return True if self.__status == 'Active' else False

    #for postflop play
    def isInHand(self):
        return True if self.__status == 'In Hand' else False

    def shouldAnalyze(self):
        return True if self.__status in ['In Hand', 'All In'] else False

    ############ Setters and Getters #############

    def getHash(self):
        return self.__hash

    def getHand(self):
        return self.__hand

    def setHand(self, hand):
        self.__hand = hand

    def setStatus(self, status):
        assert status in ['In Hand', 'Active', 'Sitting Out', 'Observing']
        self.__status = status

    ############# BETTING/REBUY/WINNING ##############

    #called by PokerGame to add money to a player's stack (e.g. when they win a pot)
    def addToStack(self, amount):
        self.__stack += amount

    #called by PokerGame to transfer money from a player's stack to the pot (e.g. for betting or posting blinds)
    def removeFromStack(self, amount):
        action = {}
        if self.__stack > amount:
            self.__stack -= amount
            action['AMOUNT'] = amount
            action['COMPLETE'] = True
        elif self.__stack < amount and self.__stack > 0:
            temp = self.__stack
            self.__stack = 0
            self.__status = 'All In'
            action['AMOUNT'] = temp
            action['COMPLETE'] = True
        else:
            self.__status = 'Sitting_Out'
            action['COMPLETE'] = False
        return action

    def rebuy(self, amount):
        if self.__stack:
            print()
        self.__stack += self.__account.withdraw(amount)

        #used to ensure stack !> max_buyin
        #if stack > :

    ################# GAMES ACTIONS ##################

    def populateActions(self, state):
        actions = ['FOLD']
        if state['currentBet'] == state['playerContribution']:
            actions.append('CHECK')
        if state['currentBet'] > state['playerContribution']:
            actions.append('CALL')
        if state['currentBet'] >= state['playerContribution']:
            actions.append('RAISE')
        return actions

    def selectAction(self, state):
        #draw user input frame
        #count down clock from 30 seconds using 'state.timer'

        #populates list of potential Actions
        actions = self.populateActions(state)
        actionString = 'Select an action: '
        for index, action in enumerate(actions):
            actionString += '{id} - {act}, '.format(id=index, act=action)

        #prompts user to select an Action
        actionSelection = None
        while True:
            actionSelection = int(input(actionString))
            if actionSelection in range(len(actions)):
                break
        action = actions[actionSelection]

        #creates new Action object based on user input
        amount = None
        if action == 'FOLD':
            action = ActionFold.Fold(self, state['street'])
            self.__status = 'Folded'
        elif action == 'CHECK':
            action = ActionCheck.Check(self, state['street'])
        elif action == 'CALL':
            toCall = state['currentBet'] - state['playerContribution']
            response = self.removeFromStack(toCall)
            #amount = toCall if self.__stack > toCall else self.__stack
            action = ActionCall.Call(self, response['AMOUNT'], state['street'])
        elif action == 'RAISE':
            low = state['minRaise'] if state['minRaise'] < self.__stack else self.__stack
            high = state['maxBet'] if state['maxBet'] else self.__stack

            while amount not in range(low, high+1):
                amount = int(input('Please a value between {low} and {high}.'.format(low=low, high=high)))
            response = self.removeFromStack(amount)
            action = ActionRaise.Raise(self, response['AMOUNT'], state['street'])
        return action

    ############ GRAPHICS #############

    def drawHand(self):
        self.__hand.draw()

    def drawAvatar(self):
        self.__account.draw()
        #CANVAS.DRAW(self.__sprite)

    def checkRep(self):
        assert self.__status in states


#player1 = Player('Nick', 200)




            #low = None
            #if state['minRaise'] == 0:
            #    low = state['bbStake']
            #elif state['minRaise'] > 0 and state['minRaise'] < self.__stack:
            #    low = state['minRaise']
            #elif state['minRaise'] >= self.__stack:
            #    low = self.__stack
