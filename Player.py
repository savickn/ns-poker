__author__ = 'Nick'


states = [
    'In Hand', #used for postflop play, e.g. player can BET/CHECK
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

    ############ Helper Methods ##############

    def isActive(self):
        return True if self.__status == 'Active' else False

    def isInHand(self):
        return True if self.__status == 'In Hand' else False

    def shouldAnalyze(self):
        return True if self.__status in ['In Hand', 'All In'] else False

    ############ Setters and Getters #############

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
        actions = []
        if state.currentBet == state.playerContribution:
            actions.append('CHECK')
        if state.currentBet >= state.playerContribution or :
            actions.append('BET')

        #if state.openedPot is False and
        return actions


    def selectAction(self, state):
        self.populateActions(state)


        #draw user input frame
        #count down clock from 30 seconds

        timer = state.timer
        min_raise = state.min_raise
        min_bet = state.min_bet


        action = input('Select an action:') #can be [CALL, BET, FOLD], RAISE/ALLIN are unnecessary
        amount = input('') #must be >2*min_raise and < self.__stack

        assert amount <= self.__stack and amount >= min_bet

        return {'ACTION': action, 'AMOUNT': amount}


    def _bet(self):
        print()

    def _call(self, amount):
        print()

    def _raise(self):
        print()


    ############ GRAPHICS #############

    def toString(self):
        return '{name}'.format(name=self.__account)

    def drawHand(self):
        self.__hand.draw()

    def drawAvatar(self):
        self.__account.draw()
        #CANVAS.DRAW(self.__sprite)

    def checkRep(self):
        assert self.__status in states


player1 = Player('Nick', 200)
