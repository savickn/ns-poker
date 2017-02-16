
from PokerCalculator import Deck


def get_connected(card1, card2):
    primary_diff = abs(card1.getHighValue() - card2.getHighValue())
    secondary_diff = None
    if(card1.getLowValue()):
        secondary_diff = abs(card1.getLowValue() - card2.getHighValue())
    if(card2.getLowValue()):
        secondary_diff = abs(card2.getLowValue() - card1.getHighValue())
    if(primary_diff == 1) or (secondary_diff == 1):
        return True

if(get_connected(Deck.ace_hearts, Deck.king_spades)):
    print('yes1')

if(get_connected(Deck.king_spades, Deck.ace_hearts)):
    print('yes2')

if(get_connected(Deck.two_spades, Deck.ace_spades)):
    print('yes3')

if(get_connected(Deck.ace_hearts, Deck.two_spades)):
    print('yes4')

if(get_connected(Deck.jack_spades, Deck.eight_clubs)):
    print('no1')


