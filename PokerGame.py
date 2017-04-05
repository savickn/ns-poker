__author__ = 'Nick'

import random
import Deck, HandPreflop, Board, Player, Account, PokerTable, Pot, ActionPostAnte, ActionPostSB, ActionPostBB
import Helpers
from collections import deque
import operator

gameOptions = {
    'ante': 0,
    'sb': 1,
    'bb': 2,
    'max_buyin': 100,
    'min_buyin': 40,
    'timer': 30
}

tableOptions = {
    'number_of_seats': 5
}

#NOT WORKING, change .update to non-mutable version
gameTypes = {
    '2NLHE': gameOptions,
    '5NLHE': gameOptions.update({'bb': 5, 'sb': 2}),
    '10NLHE': gameOptions.update({'bb': 10, 'sb': 5}),
    '10NLHEDS': gameOptions.update({'bb': 10, 'sb': 5, 'ante': 2, 'max_buyin': 400}),
    '200NLHE': gameOptions.update({'bb': 200, 'sb': 100}),
    '10PLO': gameOptions.update({'bb': 10, 'sb': 5})
}


class Poker:
    __preflop = True
    __heads_up = False
    __state = None #should be in [Running, Wait]

    __action_player = None #the player whose turn it is to act

    def __init__(self, **options):
        self.__street = None

        self.__table = PokerTable.Table(tableOptions)

        self.__deck = Deck.Deck()
        self.__board = None

        self.__cardsPerHand = 2 #or 4 in Omaha or 5 in Draw or 3 in Stud

        self.__currentBet = None #represents the most recently placed bet
        self.__minRaise = None #must be at least double the last biggest bet/raise (e.g. bet to $4 over $2 BB, bet to $20 if opponent bets $10 on the flop)
        self.__maxBet = None #mainly for Limit and PLO games


        self.__btn = None #for assigning initial positions
        self.__sb = None #for postflop play and posting blinds
        self.__bb = None #for posting blinds
        self.__fp = None #for preflop play, basically set __first_position and call __first_position.__left to move around table for betting

        ########## OPTIONS ###########

        self.__bbStake = options['bb']
        self.__sbStake = options['sb']
        self.__ante = options['ante']
        self.__maxBuyin = options['max_buyin'] * options['bb']
        self.__minBuyin = options['min_buyin'] * options['bb']
        self.__timer = options['timer']

    def checkRep(self):
        print('checkrep')

    ############## Getters and Setters ##############

    def getBoard(self):
        return self.__board

    def givePotToPlayer(self, seat):
        seat.getPlayer().addToStack(self.__pot.getPot())

    ############## Custom Getters ##############

    def getPublicState(self):
        return {
            'maxBuyIn': self.__maxBuyin,
            'minBuyIn': self.__minBuyin,
            'timer': self.__timer,
            'maxBet': self.__maxBet,
            #'minBet'1
            'bbStake': self.__bbStake,
            'street': self.__street
        }

    ############## Dealing Player Hands

    #creates a HoldemHand for each active Player, deals cards in the correct order, WORKING but refactor at some point
    def generateHands(self, activePlayers):
        #activePlayers = self.__table.getActivePlayers() #list of Players, can cache as instance var that is updated semi-regularly
        hands = [x for x in range(len(activePlayers))]

        for x in range(self.__cardsPerHand):
            for y in range(len(activePlayers)):
                if isinstance(hands[y], list):
                    hands[y].append(self.__deck.getTopCard())
                else:
                    hands[y] = [self.__deck.getTopCard()]

        seat = self.__sb
        for n in range (len(activePlayers)):
            self.dealHand(seat.getPlayer(), hands[n])
            seat = seat.getNearestLeftSeatWithActivePlayer()

    #creates player hand, maybe make it so that the hand type (e.g. Holdem vs. Omaha) depends on how many cards are passed in
    def dealHand(self, player, cards):
        hand = HandPreflop.HoldemHand(cards)
        player.setHand(hand)

    ########## Positioning Players #############

    #player with highest card becomes Button, WORKING
    def assignPositions(self):
        deck = Deck.Deck()
        deck.shuffleDeck()
        activeSeats = self.__table.getActiveSeats()

        highest = None
        for seat in activeSeats:
            card = deck.getTopCard()
            if highest is None or (card.getHighValue() > highest['Card'].getHighValue()):
                highest = {'Seat': seat, 'Card': card}
            else:
                continue

        self.__btn = highest['Seat']

        if len(activeSeats) == 2:
            self.__sb = self.__btn
        elif len(activeSeats) > 2:
            self.__sb = self.__btn.getNearestLeftSeatWithActivePlayer()

        self.__bb = self.__sb.getNearestLeftSeatWithActivePlayer()
        self.__fp = self.__bb.getNearestLeftSeatWithActivePlayer()

        #print('First Position: {seat}'.format(seat=self.__fp.toString()))
        #print('Button: {seat}'.format(seat=self.__btn.toString()))
        #print('Small Blind: {seat}'.format(seat=self.__sb.toString()))
        #print('Big Blind: {seat}'.format(seat=self.__bb.toString()))

    #used to rotate seating after each round, WORKING
    def rotatePlayers(self):
        self.__btn = self.__btn.getNearestLeftSeatWithActivePlayer()
        self.__sb = self.__sb.getNearestLeftSeatWithActivePlayer()
        self.__bb = self.__bb.getNearestLeftSeatWithActivePlayer()
        self.__fp = self.__fp.getNearestLeftSeatWithActivePlayer()

    ############ Posting SB/BB/Ante ############

    def postBB(self):
        bb = self.__bb.getPlayer()
        response = bb.removeFromStack(self.__bbStake)
        if response['COMPLETE']:
            action = ActionPostBB.PostBB(bb, response['AMOUNT'])
            self.__pot.handleAction(action)
        else:
            self.__bb = self.__bb.getNearestLeftSeatWithActivePlayer() #sets a new BB
            self.__fp = self.__bb.getNearestLeftSeatWithActivePlayer() #sets a new FP immediately left of the new BB
            self.postBB() #calls postBB until the BB is posted or an Exception is thrown

    def postSB(self):
        sb = self.__sb.getPlayer()
        response = sb.removeFromStack(self.__sbStake)
        if response['COMPLETE']:
            action = ActionPostSB.PostSB(sb, response['AMOUNT'])
            self.__pot.handleAction(action)
        else:
            self.rotatePlayers()
            self.postSB() #calls postBB until the BB is posted or an Exception is thrown

    def postAnte(self, activePlayers):
        for player in activePlayers:
            response = player.removeFromStack(self.__ante)
            if response['COMPLETE']:
                action = ActionPostAnte.PostAnte(player, response['AMOUNT'])
                self.__pot.handleAction(action)
            else:
                activePlayers.remove(player)
        return activePlayers

    ######### Community Card Actions ############

    def burnCard(self):
        self.__deck.getTopCard()

    def generateFlop(self):
        self.burnCard()
        card1 = self.__deck.getTopCard()
        card2 = self.__deck.getTopCard()
        card3 = self.__deck.getTopCard()
        self.__board = Board.Board(card1, card2, card3)
        self.__street = 'FLOP'

    def generateTurn(self):
        self.burnCard()
        card4 = self.__deck.getTopCard()
        self.__board.setTurn(card4)
        self.__street = 'TURN'

    def generateRiver(self):
        self.burnCard()
        card5 = self.__deck.getTopCard()
        self.__board.setRiver(card5)
        self.__street = 'RIVER'

    ########## Player Actions #############

    #betting begins with 'self.__fp' and continues to the left
    def preFlopBetting(self):
        self.__street = 'PREFLOP'
        startingSeat = self.__fp
        self.bettingRound(startingSeat)

    #betting begins with 'self.__sb' and continues to the left
    def postFlopBetting(self):
        startingSeat = self.__sb if self.__sb.getPlayer().isActive() else self.__sb.getNearestLeftSeatWithActivePlayer()
        self.bettingRound(startingSeat)

    #represents a single round of betting, NOT WORKING, NEED TO DISTINGUISH BETWEEN BETTING ROUNDS
    def bettingRound(self, startingSeat):
        startingSeat = startingSeat
        while True:
            activePlayer = startingSeat.getPlayer()

            #for consolidating state
            gameState = self.getPublicState()
            potState = self.__pot.getPublicState(activePlayer)
            gameState.update(potState)

            if self.__pot.hasActed(activePlayer, self.__street) and gameState['playerContribution'] == gameState['currentBet']:
                break #can be based on the number of folds or some 'winner' field

            action = activePlayer.selectAction(gameState)
            self.__pot.handleAction(action)
            startingSeat = startingSeat.getNearestLeftSeatWithActivePlayer()

    ########## Handles each individual round #############

    #used to prepare the game prior to entering the game loop
    def initializeGame(self):
        self.assignPositions()
        self.__gameState = 'RUNNING'

    #acts as the game loop
    def run(self):
        while self.__gameState == 'RUNNING':
            activePlayers = self.__table.getActivePlayers()
            if len(activePlayers) < 2:
                self.__gameState = 'WAITING'
                print('Waiting for Players')
            self.startRound(activePlayers)
            self.rotatePlayers()

    #acts as a single hand
    def startRound(self, activePlayers):
        board = None
        deck = Deck.Deck()
        deck.shuffleDeck()
        self.__pot = Pot.Pot(self.__bbStake)
        self.__pot.registerActivePlayers(activePlayers)

        self.generateHands(activePlayers)

        if self.__ante > 0:
            activePlayers = self.postAnte(activePlayers)
        self.postSB()
        self.postBB()


        print('#### PREFLOP BETTING ####')
        self.preFlopBetting()

        print('####### FLOP ########')
        self.generateFlop()
        self.__board.printAsString()
        print('#### FLOP BETTING ####')
        self.postFlopBetting()

        print('####### TURN ########')
        self.generateTurn()
        self.__board.printAsString()
        print('#### FLOP BETTING ####')
        self.postFlopBetting()

        print('####### RIVER ########')
        self.generateRiver()
        self.__board.printAsString()
        print('#### RIVER BETTING ####')
        self.postFlopBetting()

        print('####### POST-ROUND ANALYSIS #######')
        self.handleEndgame()
        return

    def handleEndgame(self):
        #activePlayers = self.__table.getPlayersToAnalyze()
        activePlayers = self.__table.getActivePlayers()
        activeHands = []

        for player in activePlayers:
            activeHands.append(player.getHand())

        winState = Helpers.determineWinner(self.__board, activeHands)
        potShare = self.__pot.getPot() * winState['EQUITY']

        #can add function to remove Rake if pot > x if necessary

        for player in activePlayers:
            if player.getHand().getCards() in winState['WINNER']:
                print(player.toString())
                print(potShare)
                player.addToStack(potShare)

    ############## Game State Manager ##############

    def areReady(self):
        readyCounter = len(self.__table.getActivePlayers())
        return True if readyCounter >= 2 else False

    #used to add a Player object to the Table
    def registerPlayer(self, player):
        assert isinstance(player, Player.Player)
        emptySeat = None
        try:
            emptySeat = self.__table.getEmptySeat()
        except:
            print('Unable to register player. There are no empty seats.')
            return
        emptySeat.setPlayer(player)

    #used to retrieve an account from the database
    def findPlayer(self, playerId):
        #find account in DB using 'player_id'... account = Account.findById(player_id)
        account = Account.findById(playerId)
        buyin = input('How much would you like to buy in for?')
        player = Player.Player(account, buyin)
        return player

    def toString(self):
        self.__table.toString()


player1 = Player.Player('Nick', 200)
player2 = Player.Player('Matt', 200)
player3 = Player.Player('Mike', 200)
player4 = Player.Player('Mark', 200)

game = Poker(**gameTypes['2NLHE'])
game.registerPlayer(player1)
game.registerPlayer(player2)
game.registerPlayer(player3)
game.registerPlayer(player4)

game.initializeGame()
game.run()


#game.assignPositions()
#game.generateHands()
game.toString()






# Rotate Players
# Post Blinds
# Check for active players
# Deal hands to active players (and change state to In Hand)
# Pass control to preflop betting round
# If >= 2 players are In Hand, Deal flop
# Pass control to postflop betting round
# If >= 2 players are In Hand, Deal turn
# Pass control to postflop betting round
# If >= 2 players are In Hand, Deal river
# Pass control to postflop betting round
# If >= 2 players are In Hand, show hands + award pot to winner
# Call reset



# def play(self):
#         self.generateHands()
#         self.__preflop = True
#
#         #action = self.__utg.selectAction(self.getPublicState())
#         #self.handle_action(self.__utg, action)
#
#         #add betting action at some point
#         self.generateFlop()
#         self.__preflop = False
#         self.generateTurn()

# def reset(self):
#         self.__board = None
#         self.__pot = 0
#         self.__preflop = True
#         self.__deck.shuffleDeck()
#         self.rotate_players()

    # def postBB(self):
    #     response = self.__bb.getPlayer().removeFromStack(self.__bbStake)
    #     if response['COMPLETE']:
    #         self.__pot += response['AMOUNT']
    #         if self.__bbStake > self.__currentBet:
    #             self.__currentBet = self.__bbStake

#__players = None #organized as follows: [UTG, UTG2, UTG3, LOJ, HIJ, CO, BTN, SB, BB]
    #__playerMap = {}
    #__seats = None