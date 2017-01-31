__author__ = 'Nick'

class Seat:
    __id = None
    __player = None
    __right = None
    __left = None
    #__role? e.g. btn vs. sb vs. bb

    def __init__(self, id, right=None, left=None):
        self.__id = id
        self.__right = right
        self.__left = left

    #maybe change to getActiveLeft where it finds the nearest person that is Active
    def getNearestLeftSeatWithActivePlayer(self):
        temp = self.__left
        for num in range (1, 11):
            player = temp.getPlayer()
            if player.getStatus() is 'Active' and player is not self.__player:
                return temp
            else:
                temp = temp.__left

        return 'Not enough players are active.'

    ############# GETTERS ##############

    def getId(self):
        return self.__id

    def getPlayer(self):
        return self.__player

    def getLeft(self):
        return self.__left

    def getRight(self):
        return self.__right

    ########### SETTERS #############

    def setLeft(self, player):
        self.__left = player

    def setRight(self, player):
        self.__right = player

    def setPlayer(self, player):
        self.__player = player

    ########### Utility ###############

    def toString(self):
        return 'Seat-{id}, Left = Seat-{lid}, Right = Seat-{rid}'.format(id=self.__id, lid=self.__left.getId(), rid=self.__right.getId())

    def checkRep(self):
        print()
