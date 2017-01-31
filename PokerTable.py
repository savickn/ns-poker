__author__ = 'Nick'

from PokerCalculator import Seat

boilerplate_options = {
    'number_of_seats': 9
}

class Table:
    #figure out how to dynamically create Seats based on how type of table (e.g. 6-max vs. HU vs. full-ring)
    __seats = None

    def __init__(self, options={}):
        assert options['number_of_seats'] >= 2
        self.__seats = self.setSeats(options['number_of_seats'])
        self.checkRep()

    #for debugging only
    def getSeats(self):
        for seat in self.__seats:
            print(seat)

    #for initializing and changing the table's Seats
    def setSeats(self, number_of_seats):
        seats = []
        iterator = 1
        right_seat = None
        while iterator <= number_of_seats:
            if right_seat is not None:
                seat = Seat.Seat(iterator, right_seat)
                seats.append(seat)
                right_seat.setLeft(seat) #working
                right_seat = seat
                iterator += 1
            else:
                seat = Seat.Seat(iterator)
                seats.append(seat)
                right_seat = seat
                iterator += 1

        first_seat = seats[0]
        last_seat = seats[len(seats)-1]

        first_seat.setRight(last_seat)
        last_seat.setLeft(first_seat)

        return tuple(seats)

    def addSeat(self):
        assert len(self.__seats) <= 10

        seats = list(self.__seats)
        first_seat = seats[0]
        last_seat = seats[len(seats)-1]

        new_seat = Seat.Seat(len(seats)+1, last_seat, first_seat)
        seats.append(new_seat)
        self.__seats = tuple(seats)

    def removeSeat(self):
        assert len(self.__seats) >= 2
        print('remove seat')

    #used to determine which players are involved in a hand
    def countActivePlayers(self):
        players = self.getActivePlayers()
        return len(players)

    def getActivePlayers(self):
        players = []
        for seat in self.__seats:
            player = seat.getPlayer()
            if player is not None and player.getStatus() is 'Active':
                players.append(player)
        return players

    def getAllPlayers(self):
        players = []
        for seat in self.__seats:
            player = seat.getPlayer()
            if player is not None:
                players.append(player)
        return players

    ############## Utility Methods #################

    def checkRep(self):
        assert len(self.__seats) >=2 and len(self.__seats) <= 9
        #assert self.__game in self.__game_types
        #also assert that there are no duplicate players

    def toString(self):
        for seat in self.__seats:
            print(seat.toString())

table = Table(boilerplate_options)
table.toString()
#table.getSeats()


    #creates an instance of the poker game (e.g. Holdem vs. Omaha)
    #__game = None
    #__game_types = ["NLHE", "PLO"]
    #self.__game = self.createGame()
