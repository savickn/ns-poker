__author__ = 'Nick'

from PokerCalculator import Card, Deck, PreflopHand, Board, Range, Avatar, Account

class Player:
    __account = None
    __stack = None
    __range = None
    __status = None #must be in [ACTIVE, SITTING_OUT]
    __hand = None #can be an Omaha or Texas Holdem hand

    def __init__(self, buyin, account=''):
        #self.__account = account
        #self.__stack = account.withdraw(buyin)
        self.__stack = buyin
        self.__status = 'Active'
        #self.__range = Range.Range()

        print('player init')

    def checkRep(self):
        assert self.__status in ['In Hand', 'Active', 'Sitting Out', 'Observing']

    ############ Setters and Getters #############

    def setHand(self, hand):
        self.__hand = hand

    def getHand(self):
        return self.__hand

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        assert self.__status in ['In Hand', 'Active', 'Sitting Out', 'Observing']
        self.__status = status

    ############# Interact with game ##############

    #called by PokerGame to add money to a player's stack (e.g. when they win a pot)
    def addToStack(self, amount):
        self.__stack += amount

    #called by PokerGame to transfer money from a player's stack to the pot (e.g. for betting or posting blinds)
    def removeFromStack(self, amount):
        if self.__stack > amount:
            self.__stack -= amount
            return True
        elif self.__stack < amount and self.__stack > 0:
            temp = self.__stack
            self.__stack = 0
            return True
        else:
            self.__status = 'Sitting_Out'
            return False




    def rebuy(self, amount):
        if self.__stack:
            print()
        self.__stack += self.__account.withdraw(amount)

        #used to ensure stack !> max_buyin
        #if stack > :

    #maybe instead use generic 'post_mandatory_bet'


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


    ####### Graphics

    def draw_hand(self):
        self.__hand.draw()

    def draw_avatar(self):
        self.__account.draw()
        #CANVAS.DRAW(self.__sprite)


player1 = Player(200)
