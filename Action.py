__author__ = 'Nick'



class Action:

    def __init__(self, actor, amount, street):
        self.__actor = actor
        self.__amount = amount
        self.__street = street

        #__hash = None #used to validate that the same Action was returned
        #__completed = False #used to determine if the action was satisfied by the target

    def getActor(self):
        return self.__actor

    def getAmount(self):
        return self.__amount

    def getStreet(self):
        return self.__street


