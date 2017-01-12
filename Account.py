__author__ = 'Nick'

from PokerCalculator import Avatar

class Account:
    __username = None
    __email = None
    __password = None
    __country = None
    __status = None
    __balance = None
    __sprite = None

    def __init__(self, username, email, password, country):
        self.__username = username
        self.__email = email
        self.__password = password
        self.__country = country
        self.__balance = 0

    #also write functions to add/take money to/from a bank account

    def login(self, email, password):
        if self.__email == email and self.__password == password:
            self.__status = 'Logged In'
            return True
        else:
            print('The information you entered was incorrect.')
            return False

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def setSprite(self, image):
        self.__sprite = Avatar.Avatar(image)

    def draw(self):
        self.__sprite.draw()