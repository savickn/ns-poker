__author__ = 'Nick'


from PokerCalculator import Deck, Board

class Poker:
    __deck = None
    __board = None

    def __init__(self):
        self.__deck = Deck.Deck()

    def getBoard(self):
        return self.__board

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

game = Poker()
game.generateFlop()
game.getBoard().printAsString()
game.generateTurn()
game.getBoard().printAsString()
game.generateRiver()
game.getBoard().printAsString()