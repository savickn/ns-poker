__author__ = 'Nick'

import random
from PokerCalculator import Card, Deck, PreflopHand, Board, Player, Account
from collections import deque

boilerplate_options = {
    'ante': 0,
    'sb': 1,
    'bb': 2,
    'max_buyin': 100,
    'min_buyin': 40,
    'action_timer': 30
}

class Poker:
    __preflop = True
    __heads_up = False

    __max_buyin = None
    __min_buyin = None

    __action_player = None #the player whose turn it is to act
    __action_timer = None

    __bb_stake = None
    __sb_stake = None
    __ante = None

    __players = None #organized as follows: [UTG, UTG2, UTG3, LOJ, HIJ, CO, BTN, SB, BB]
    __playerMap = {}

    __deck = None
    __board = None
    __pot = 0

    __min_raise = None #must be at least double the last biggest bet/raise (e.g. bet to $4 over $2 BB, bet to $20 if opponent bets $10 on the flop)
    __max_bet = None

    def __init__(self, players=[], **options):
        self.__players = deque(players)
        self.__deck = Deck.Deck()

        self.__bb_stake = options['bb']
        self.__sb_stake = options['sb']
        self.__ante = options['ante']

        self.__max_buyin = options['max_buyin']*options['bb']
        self.__min_buyin = options['min_buyin']*options['bb']

    ############## Getters and Setters ##############

    def getPot(self):
        return self.__pot

    #def addToPot(self, amount):
    #    self.__pot += amount

    def getPlayers(self):
        return self.__players

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

    def generateHands(self):
        num = len(self.__players)

        sb = self.__players[num - 2]
        bb = self.__players[num - 1]
        btn = self.__players[num - 3]
        co = self.__players[num - 4]
        hij = self.__players[num - 5]
        loj = self.__players[num - 6]
        utg3 = self.__players[num - 7]
        utg2 = self.__players[num - 8]
        utg = self.__players[num - 9]

        cards = {
            sb: [],
            bb: [],
            btn: [],
            co: [],
            hij: [],
            loj: [],
            utg3: [],
            utg2: [],
            utg: []
        }

        cards[sb].append(self.dealCard())
        cards[bb].append(self.dealCard())
        cards[utg].append(self.dealCard())
        cards[utg2].append(self.dealCard())
        cards[utg3].append(self.dealCard())
        cards[loj].append(self.dealCard())
        cards[hij].append(self.dealCard())
        cards[co].append(self.dealCard())
        cards[btn].append(self.dealCard())

        cards[sb].append(self.dealCard())
        cards[bb].append(self.dealCard())
        cards[utg].append(self.dealCard())
        cards[utg2].append(self.dealCard())
        cards[utg3].append(self.dealCard())
        cards[loj].append(self.dealCard())
        cards[hij].append(self.dealCard())
        cards[co].append(self.dealCard())
        cards[btn].append(self.dealCard())

        self.dealHand(sb, cards[sb])
        self.dealHand(bb, cards[bb])
        self.dealHand(utg, cards[utg])
        self.dealHand(utg2, cards[utg2])
        self.dealHand(utg3, cards[utg3])
        self.dealHand(loj, cards[loj])
        self.dealHand(hij, cards[hij])
        self.dealHand(co, cards[co])
        self.dealHand(btn, cards[btn])

    #first card goes to the SB
    def dealCard(self):
        return self.__deck.getTopCard()

    #creates player hand, maybe make it so that the hand type (e.g. Holdem vs. Omaha) depends on how many cards are passed in
    def dealHand(self, player, cards):
        hand = PreflopHand.HoldemHand(cards[0], cards[1])
        player.setHand(hand)

    ########## Positioning Players #############

    #player with highest card becomes Button
    def assignPositions(self):
        self.__deck.shuffleDeck()
        player_cards = {}

        for player in self.__players:
            player_cards[player] = self.__deck.getTopCard()
            #print(player)
            #print(player_cards[player])

        sorted_cards = sorted(player_cards.values(), reverse=True)

        #player_cards = sorted(player_cards, key=player.getPrimaryValue() in player_cards)

        for player in player_cards:
            if player_cards[player].getPrimaryValue() is sorted_cards[0]:
                self.__playerMap['btn'] = player

        print(self.__playerMap['btn'])


    def rotate_players(self):
        self.__players.rotate(1)


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

    def add_to_pot(self, amount):
        self.__pot += amount

    actions = ['POST_BB', 'POST_SB', 'POST_ANTE', 'YOUR_TURN']

    def prompt_for_bb(self):
        print()

        #if self.__bb.post_bet(self.__bb_stake):
        #    self.__last_bet = self.__sb_stake

    def prompt_for_sb(self):
        print()
        #if self.__sb.post_bet(self.__sb_stake):
        #    self.__last_bet = self.__sb_stake

    def prompt_for_ante(self):
        for player in self.__players:
            player.post_bet(self.__ante)

    def preFlopBetting(self):
        print('not implemented')

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








