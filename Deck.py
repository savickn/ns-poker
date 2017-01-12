__author__ = 'Nick'

from PokerCalculator import Card, PreflopHand
import random

ace_hearts = Card.Card('Ace', 'Hearts', 14, {'secondary_value': 1})
king_hearts = Card.Card('King', 'Hearts', 13)
queen_hearts = Card.Card('Queen', 'Hearts', 12)
jack_hearts = Card.Card('Jack', 'Hearts', 11)
ten_hearts = Card.Card('Ten', 'Hearts', 10)
nine_hearts = Card.Card('Nine', 'Hearts', 9)
eight_hearts = Card.Card('Eight', 'Hearts', 8)
seven_hearts = Card.Card('Seven', 'Hearts', 7)
six_hearts = Card.Card('Six', 'Hearts', 6)
five_hearts = Card.Card('Five', 'Hearts', 5)
four_hearts = Card.Card('Four', 'Hearts', 4)
three_hearts = Card.Card('Three', 'Hearts', 3)
two_hearts = Card.Card('Two', 'Hearts', 2)
ace_spades = Card.Card('Ace', 'Spades', 14, {'secondary_value': 1})
king_spades = Card.Card('King', 'Spades', 13)
queen_spades = Card.Card('Queen', 'Spades', 12)
jack_spades = Card.Card('Jack', 'Spades', 11)
ten_spades = Card.Card('Ten', 'Spades', 10)
nine_spades = Card.Card('Nine', 'Spades', 9)
eight_spades = Card.Card('Eight', 'Spades', 8)
seven_spades = Card.Card('Seven', 'Spades', 7)
six_spades = Card.Card('Six', 'Spades', 6)
five_spades = Card.Card('Five', 'Spades', 5)
four_spades = Card.Card('Four', 'Spades', 4)
three_spades = Card.Card('Three', 'Spades', 3)
two_spades = Card.Card('Two', 'Spades', 2)
ace_clubs = Card.Card('Ace', 'Clubs', 14, {'secondary_value': 1})
king_clubs = Card.Card('King', 'Clubs', 13)
queen_clubs = Card.Card('Queen', 'Clubs', 12)
jack_clubs = Card.Card('Jack', 'Clubs', 11)
ten_clubs = Card.Card('Ten', 'Clubs', 10)
nine_clubs = Card.Card('Nine', 'Clubs', 9)
eight_clubs = Card.Card('Eight', 'Clubs', 8)
seven_clubs = Card.Card('Seven', 'Clubs', 7)
six_clubs = Card.Card('Six', 'Clubs', 6)
five_clubs = Card.Card('Five', 'Clubs', 5)
four_clubs = Card.Card('Four', 'Clubs', 4)
three_clubs = Card.Card('Three', 'Clubs', 3)
two_clubs = Card.Card('Two', 'Clubs', 2)
ace_diamonds = Card.Card('Ace', 'Diamonds', 14, {'secondary_value': 1})
king_diamonds = Card.Card('King', 'Diamonds', 13)
queen_diamonds = Card.Card('Queen', 'Diamonds', 12)
jack_diamonds = Card.Card('Jack', 'Diamonds', 11)
ten_diamonds = Card.Card('Ten', 'Diamonds', 10)
nine_diamonds = Card.Card('Nine', 'Diamonds', 9)
eight_diamonds = Card.Card('Eight', 'Diamonds', 8)
seven_diamonds = Card.Card('Seven', 'Diamonds', 7)
six_diamonds = Card.Card('Six', 'Diamonds', 6)
five_diamonds = Card.Card('Five', 'Diamonds', 5)
four_diamonds = Card.Card('Four', 'Diamonds', 4)
three_diamonds = Card.Card('Three', 'Diamonds', 3)
two_diamonds = Card.Card('Two', 'Diamonds', 2)

deck = [
    ace_hearts,
    king_hearts,
    queen_hearts,
    jack_hearts,
    ten_hearts,
    nine_hearts,
    eight_hearts,
    seven_hearts,
    six_hearts,
    five_hearts,
    four_hearts,
    three_hearts,
    two_hearts,
    ace_clubs,
    king_clubs,
    queen_clubs,
    jack_clubs,
    ten_clubs,
    nine_clubs,
    eight_clubs,
    seven_clubs,
    six_clubs,
    five_clubs,
    four_clubs,
    three_clubs,
    two_clubs,
    ace_diamonds,
    king_diamonds,
    queen_diamonds,
    jack_diamonds,
    ten_diamonds,
    nine_diamonds,
    eight_diamonds,
    seven_diamonds,
    six_diamonds,
    five_diamonds,
    four_diamonds,
    three_diamonds,
    two_diamonds,
    ace_spades,
    king_spades,
    queen_spades,
    jack_spades,
    ten_spades,
    nine_spades,
    eight_spades,
    seven_spades,
    six_spades,
    five_spades,
    four_spades,
    three_spades,
    two_spades
]

class Deck:
    __cards = None
    __length = None

    def __init__(self):
        self.__cards = deck
        self.__length = len(self.__cards)
        self.checkRep()
        print('deck init')

    def shuffleDeck(self):
        self.__cards = self.shuffle(self.__cards)
        self.refreshLength()

    def shuffle(self, cards):
        ary = cards
        a=len(ary)
        b=a-1
        for d in range(b,0,-1):
          e=random.randint(0,d)
          if e == d:
                continue
          ary[d],ary[e]=ary[e],ary[d]
        return ary

    def getTopCard(self):
        card =  self.__cards.pop(0)
        self.__length = len(self.__cards)
        return card

    def getHandCombos(self):
        #__unsuitedCombos = None
        #__suitedCombos = None
        #__totalCombos = None
        print('handcombos')

    def refreshLength(self):
        self.__length = len(self.__cards)
        print('refresh hand combos')

    def checkRep(self):
        assert self.__length <= 52 and self.__length >= 0


#d = Deck()
#c = d.getTopCard()
#print(c.getState())
#c.setState(False)
#print(c.getState())

#d = Deck()
#c = d.getTopCard()
#print(c.getState())

