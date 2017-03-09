__author__ = 'Nick'

import Account

#represents the main browser than can be used to login to an account or find games
class Client:
    __account = None
    __mainView = None

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