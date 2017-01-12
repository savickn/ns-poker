__author__ = 'Nick'

from PokerCalculator import PokerGame

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

class Table:
    #creates an instance of the poker game (e.g. Holdem vs. Omaha)
    __game = None
    __game_types = ["NLHE", "PLO"]

    #figure out how to dynamically create Seats based on how type of table (e.g. 6-max vs. HU vs. full-ring)
    __seats = None


    def __init__(self):
        self.__game = self.createGame()

    def __getPlayers(self):
        players = []

        if self.__seat1 is not None:
            players.append(self.__seat1)
        if self.__seat2 is not None:
            players.append(self.__seat2)
        if self.__seat3 is not None:
            players.append(self.__seat3)
        if self.__seat4 is not None:
            players.append(self.__seat4)
        if self.__seat5 is not None:
            players.append(self.__seat5)
        if self.__seat6 is not None:
            players.append(self.__seat6)
        if self.__seat7 is not None:
            players.append(self.__seat7)
        if self.__seat8 is not None:
            players.append(self.__seat8)
        if self.__seat9 is not None:
            players.append(self.__seat9)

        return players

    #user clicks on an empty seat
    def joinTable(self, seat, player):
        self.seat = player

    def createGame(self):
        game_type = input('Please select the game type.')
        assert game_type in self.__game_types

        #for custom games
        #options = {}
        #options['bb'] = input('')
        #options['sb'] = input('')
        #options['ante'] = input('')
        #options['max_buyin'] = input('')
        #options['min_buyin'] = input('')

        if game_type == 'NLHE':
            #self.__game = Poker(self.__players, **options)
            self.__game = PokerGame.Poker(self.__getPlayers(), boilerplate_options)
            self.__game.assign_positions(self.__getPlayers())
        elif game_type == 'PLO':
            print('PLO not implemented')
        else:
            raise Exception('The game type you entered is not valid.')

    def startGame(self):
        if self.areReady():
            self.__game.play()

    def areReady(self):
        ready_counter = 0
        for player in self.__players:
            if player.getStatus() is 'Active':
                ready_counter += 1
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

    def checkRep(self):
        print('checkrep')
        #assert self.__game in self.__game_types
        #also assert that there are no duplicate players