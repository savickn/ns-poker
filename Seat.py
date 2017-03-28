__author__ = 'Nick'

class Seat:
    __id = None
    __player = None
    __right = None
    __left = None

    def __init__(self, id, right=None, left=None):
        self.__id = id
        self.__right = right
        self.__left = left

    ################ HELPER METHODS #################

    #maybe change to getActiveLeft where it finds the nearest person that is Active
    def getNearestLeftSeatWithActivePlayer(self):
        temp = self.__left
        for num in range (10):
            player = temp.getPlayer()
            if player is not None and player.isActive() and player is not self.__player:
                return temp
            else:
                temp = temp.getLeft()
        raise Exception('There are not enough ACTIVE players.')

    #used to choose an empty Seat when adding a new Player to the Table
    def isEmpty(self):
        return True if not self.__player else False

    ################# GETTERS ###############

    def getId(self):
        return self.__id

    def getPlayer(self):
        return self.__player

    def getLeft(self):
        return self.__left

    def getRight(self):
        return self.__right

    ################ SETTERS ################

    def setLeft(self, player):
        self.__left = player

    def setRight(self, player):
        self.__right = player

    def setPlayer(self, player):
        assert self.isEmpty()
        self.__player = player

    ################ Utility ################

    def toString(self):
        player = self.__player.toString() if self.__player else 'Empty'
        return '{player} sitting in Seat-{id}... Left = Seat-{lid}, Right = Seat-{rid}'.format(player=player, id=self.__id, lid=self.__left.getId(), rid=self.__right.getId())

    def checkRep(self):
        print()
