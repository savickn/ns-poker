__author__ = 'Nick'


states = [
    'In Hand', #will be given a chance to BET/CHECK
    'All In', #will be analyzed after RIVER but will not be given a chance to BET/CHECK
    'Active', #will be dealt a hand
    'Sitting Out' #will not be dealt a hand
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
        self.__status = 'Sitting Out' #must be in [ACTIVE, SITTING_OUT]
        self.__hand = None #can be an Omaha or Texas Holdem hand

        self.__timeBank = None
        self.__tableView = None #must be initialized when Player joins using Game.getPublicInfo

        self.__stack = buyin
        #self.__stack = account.withdraw(buyin)


        #self.__utgRange = options['UTG'] if options['UTG'] else []
        #self.__coRange = options['CO'] if options['CO'] else []
        #self.__btnRange = options['BTN'] if options['BTN'] else []
        #self.__sbRange = options['SB'] if options['SB'] else []
        #self.__bbRange = options['BB'] if options['BB'] else []


    ############ Setters and Getters #############

    def setHand(self, hand):
        self.__hand = hand

    def getHand(self):
        return self.__hand

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        assert status in ['In Hand', 'Active', 'Sitting Out', 'Observing']
        self.__status = status

    ############# Interact with game ##############

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


    def selectAction(self, state):
        #draw user input frame
        #count down clock from 30 seconds

        timer = state.timer
        min_raise = state.min_raise
        min_bet = state.min_bet

        action = input('') #can be [BET, FOLD, CALL, RAISE, ALLIN]
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

    def drawHand(self):
        self.__hand.draw()

    def drawAvatar(self):
        self.__account.draw()
        #CANVAS.DRAW(self.__sprite)

    def checkRep(self):
        assert self.__status in states


player1 = Player('Nick', 200)
