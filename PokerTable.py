__author__ = 'Nick'

import Seat
from tkinter import *
from tkinter.ttk import *

default = {
    'number_of_seats': 4
}

class Table:

    def __init__(self, options=default):
        #figure out how to dynamically create Seats based on how type of table (e.g. 6-max vs. HU vs. full-ring)
        self.__seats = self.initializeSeats(options['number_of_seats'])
        self.__observers = [] #Players that are observing the table
        self.__waitlist = [] #Players that are waiting to join the table
        self.checkRep()

        self.draw()


    ############### HANDLING SEATS #################

    #for registering players, WORKING
    def getEmptySeat(self):
        for seat in self.__seats:
            if seat.isEmpty():
                return seat
        raise Exception('There are no empty seats.')

    #for initializing and changing the table's Seats, returns a Tuple, WORKING
    def initializeSeats(self, number_of_seats):
        seats = []
        rightSeat = None
        for it in range(number_of_seats):
            if rightSeat is not None:
                seat = Seat.Seat(it+1, rightSeat)
                seats.append(seat)
                rightSeat.setLeft(seat) #working
                rightSeat = seat
            else:
                seat = Seat.Seat(it+1)
                seats.append(seat)
                rightSeat = seat

        firstSeat = seats[0]
        lastSeat = seats[len(seats)-1]
        firstSeat.setRight(lastSeat)
        lastSeat.setLeft(firstSeat)

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
        for seat in self.__seats:
            if seat.isEmpty():
                print()
                return

    ############### HANDLING PLAYERS #################

    #returns all Seats that contain a Player
    def getFilledSeats(self):
        seats = [seat for seat in self.__seats if seat.getPlayer() is not None]
        return seats

    #returns all Players currently sitting at the Table
    def getPlayers(self):
        players = []
        for seat in self.__seats:
            player = seat.getPlayer()
            if player is not None:
                players.append(player)
        return players

    def getActiveSeats(self):
        seats = []
        for seat in self.__seats:
            player = seat.getPlayer()
            if player is not None and player.isActive():
                seats.append(seat)
        return seats

    #used to determine which players should be dealt-in pre-flop
    def getActivePlayers(self):
        players = []
        for seat in self.__seats:
            player = seat.getPlayer()
            if player is not None and player.isActive():
                players.append(player)
        return players

    def getPlayersToAnalyze(self):
        players = []
        for seat in self.__seats:
            player = seat.getPlayer()
            if player is not None and player.shouldAnalyze():
                players.append(player)
        return players

    #used to determine which players are involved in the hand post-flop
    def getInHandPlayers(self):
        players = []
        for seat in self.__seats:
            player = seat.getPlayer()
            if player is not None and player.isInHand():
                players.append(player)
        return players


    ################ Utility Methods ##################

    def checkRep(self):
        assert len(self.__seats) >=2 and len(self.__seats) <= 9
        #assert self.__game in self.__game_types
        #also assert that there are no duplicate players

    def toString(self):
        for seat in self.__seats:
            print(seat.toString())

    #for debugging only
    def getSeats(self):
        for seat in self.__seats:
            print(seat)

    ############### GRAPHICS ##############

    def draw(self):
        #draw table
        self.drawTable()


        #draw seats
        for s in self.__seats:
            self.drawSeat(s)

    def drawTable(self):

        print()

    def drawSeat(self, seat):
        seat.draw()

#table = Table(default)
#table.toString()
#table.getSeats()


    #creates an instance of the poker game (e.g. Holdem vs. Omaha)
    #__game = None
    #__game_types = ["NLHE", "PLO"]
    #self.__game = self.createGame()


#returns all Seats that contain a Player
    # def getFilledSeats(self):
    #     seats = []
    #     for seat in self.__seats:
    #         if seat.getPlayer() is not None:
    #             seats.append(seat)
    #     return seats