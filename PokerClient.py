__author__ = 'Nick'

from PokerCalculator import Account

class Client:
    __account = None

    def logIn(self):
        email = input('Please enter your email address.')
        password = input('Please enter your password.')
        #query DB for 'email' and validate that password matches... self.__account = Account

    def createAccount(self):
        username = input('Please enter your username.')
        email = input('Please enter your email address.')
        password = input('Please enter your password.')
        country = input('Please select a country.')
        player = Account.Account(username, email, password, country)
        #save player to DB