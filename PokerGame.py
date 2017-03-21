__author__ = 'Nick'

import random
import Card, Deck, HandPreflop, Board, Player, Account, PokerTable
from collections import deque

boilerplate_options = {
    'ante': 0,
    'sb': 1,
    'bb': 2,
    'max_buyin': 100,
    'min_buyin': 40,
    'action_timer': 30
}

gameTypes = {
    '2NLHE': boilerplate_options,
    '5NLHE': boilerplate_options.update({'bb': 5, 'sb': 2}),
    '10NLHE': boilerplate_options.update({'bb': 10, 'sb': 5}),
    '10NLHEDS': boilerplate_options.update({'bb': 10, 'sb': 5, 'ante': 2, 'max_buyin': 400}),
    '200NLHE': boilerplate_options.update({'bb': 200, 'sb': 100}),
    '10PLO': boilerplate_options.update({'bb': 10, 'sb': 5})
}


class Poker:
    __preflop = True
    __heads_up = False
    __cardsPerHand = 2 #or 4 in Omaha or 5 in Draw or 3 in Stud
    __state = None #should be in [Running, Wait]

    __action_player = None #the player whose turn it is to act
    __action_timer = None


    #__players = None #organized as follows: [UTG, UTG2, UTG3, LOJ, HIJ, CO, BTN, SB, BB]
    #__playerMap = {}
    #__seats = None

    __btn = None #for assigning initial positions
    __sb = None #for postflop play and posting blinds
    __bb = None #for posting blinds
    __fp = None #for preflop play, basically set __first_position and call __first_position.__left to move around table for betting

    __deck = None
    __board = None
    __pot = 0

    __current_bet = None #represents the most recently placed bet
    __min_raise = None #must be at least double the last biggest bet/raise (e.g. bet to $4 over $2 BB, bet to $20 if opponent bets $10 on the flop)
    __max_bet = None #mainly for Limit and PLO games

    def __init__(self, **options):
        #self.__players = deque(players)
        #self.__seats = seats
        # self.__deck = Deck.Deck()


        self.__table = PokerTable.Table()


        ########## OPTIONS ###########

        self.__bb_stake = options['bb']
        self.__sb_stake = options['sb']
        self.__ante = options['ante']
        self.__max_buyin = options['max_buyin']*options['bb']
        self.__min_buyin = options['min_buyin']*options['bb']

    def checkRep(self):
        print('checkrep')

    ############## Getters and Setters ##############

    def getBoard(self):
        return self.__board

    def addToPot(self, amount):
        self.__pot += amount

    def givePotToPlayer(self, seat):
        seat.getPlayer().addToStack(self.__pot)
        self.__pot = 0

    ############## Custom Getters ##############

    def getPublicState(self):
        return {
            'max_buyin': self.__max_buyin,
            'min_buyin': self.__min_buyin,
            'timer': self.__action_timer,
            'min_raise': self.__min_raise,
            'min_bet': self.__bb_stake
        }

    ############## Dealing Player Hands

    #creates a HoldemHand for each active Player, deals cards in the correct order
    def generateHands(self):
        activePlayers = self.__table.getActivePlayers() #list of Players
        numberOfActivePlayers = len(activePlayers)
        hands = {}

        for x in range(self.__cardsPerHand):
            for y in range(numberOfActivePlayers):
                hands['hand' + str(y)] = []
                hands['hand' + str(y)].append(self.__deck.getTopCard())

        first_seat = self.__sb
        it = 1
        for num in range (0, len(activePlayers)):
            cards = hands['hand{id}'.format(id=it)]
            self.dealHand(first_seat.getPlayer(), cards)
            first_seat = first_seat.getLeft()
            it += 1

    #creates player hand, maybe make it so that the hand type (e.g. Holdem vs. Omaha) depends on how many cards are passed in
    def dealHand(self, player, cards):
        hand = HandPreflop.HoldemHand(cards)
        player.setHand(hand)

    ########## Positioning Players #############

    #player with highest card becomes Button
    def assignPositions(self):
        self.__deck.shuffleDeck()
        player_cards = {}

        for seat in self.__table.getActiveSeats():
            player_cards[seat.getPlayer()] = self.__deck.getTopCard()
            #print(player)
            #print(player_cards[player])

        sorted_cards = sorted(player_cards.values(), reverse=True)
        keys = sorted_cards.keys()
        #print(keys[0])

        self.__btn = keys[0]

        active_seats = self.__table.getActiveSeats()
        if active_seats is 2:
            self.__sb = self.__btn
        elif active_seats > 2:
            self.__sb = self.__btn.getActiveLeft()

        self.__bb = self.__sb.getActiveLeft()
        self.__fp = self.__bb.getActiveLeft()

    #rotates players after each round
    def rotate_players(self):
        self.__sb = self.__sb.getNearestLeftSeatWithActivePlayer()
        self.__bb = self.__bb.getNearestLeftSeatWithActivePlayer()
        self.__fp = self.__fp.getNearestLeftSeatWithActivePlayer()

    ######### Community Card Actions ############

    def burnCard(self):
        self.__deck.getTopCard()

    def generateFlop(self):
        self.burnCard()
        card1 = self.__deck.getTopCard()
        card2 = self.__deck.getTopCard()
        card3 = self.__deck.getTopCard()
        self.__board = Board.Board(card1, card2, card3)

    def generateTurn(self):
        self.burnCard()
        card4 = self.__deck.getTopCard()
        self.__board.setTurn(card4)

    def generateRiver(self):
        self.burnCard()
        card5 = self.__deck.getTopCard()
        self.__board.setRiver(card5)

    ############ Calling/Raising/Posting SB/BB/Ante ############

    actions = ['POST_BB', 'POST_SB', 'POST_ANTE', 'YOUR_TURN']

    def prompt_for_bb(self):
        if self.__bb.getPlayer().removeFromStack(self.__bb_stake):
            self.__pot += self.__bb_stake
            if self.__bb_stake > self.__last_bet:
                self.__last_bet = self.__bb_stake
        else:
            print()
            #must reassign position if fails

    def prompt_for_sb(self):
        if self.__sb.getPlayer().removeFromStack(self.__sb_stake):
           self.__pot += self.__sb_stake
           if self.__sb_stake > self.__last_bet:
                    self.__last_bet = self.__sb_stake
        else:
            print()
            #must reassign position if fails

    def prompt_for_ante(self):
        for player in self.__table.getActivePlayers():
            if player.removeFromStack(self.__ante):
                self.__pot += self.__ante
                if self.__ante > self.__last_bet:
                    self.__last_bet = self.__ante

    ########## Handles each individual round #############

    def startRound(self):
        if self.__ante > 0:
            self.prompt_for_ante()
        self.prompt_for_sb()
        self.prompt_for_bb()

        active_players = self.__table.getActivePlayers()
        #condition for if active_players < 2




    ########## Preflop Actions #############

    def preFlopBetting(self):


        num = 1
        player = self.__fp.getPlayer()
        action = player.selectAction(self.getPublicState())
        self.handle_action(player, action)

        while num < self.__table.countActivePlayers():
            print()

        print('not implemented')

    ######### Postflop Actions #############

    def postFlopBetting(self):
        print('not implemented')

    def handle_action(self, player, action):
        if action.ACTION is ('BET' or 'RAISE' or 'CALL'):
            if player.removeFromStack(action.AMOUNT):
                self.__pot += action.AMOUNT
        elif action.ACTION is 'FOLD':
            player.setStatus('Active')
        else:
            raise Exception('This action is not recognized.')


    ############## Game State Manager ##############

    def reset(self):
        self.__board = None
        self.__pot = 0
        self.__preflop = True
        self.__deck.shuffleDeck()
        self.rotate_players()

    def play(self):
        self.generateHands()
        self.__preflop = True

        #action = self.__utg.selectAction(self.getPublicState())
        #self.handle_action(self.__utg, action)

        #add betting action at some point
        self.generateFlop()
        self.__preflop = False
        self.generateTurn()

    def areReady(self):
        ready_counter = self.__table.getActiveSeats()
        if ready_counter >= 2:
            return True
        else:
            return False

    def registerPlayer(self, player_id):
        #find account in DB using 'player_id'... account = Account.findById(player_id)
        print('register stub')

        #account = Account.findById(player_id)
        #buyin = input('How much would you like to buy in for?')
        #player = Player(account, buyin)
        #self.__players.add(player)




player1 = Player.Player(200)
player2 = Player.Player(200)
players = []
players.append(player1)
players.append(player2)

game = Poker(players, **boilerplate_options)
game.assignPositions()



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








