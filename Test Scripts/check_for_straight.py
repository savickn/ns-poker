__author__ = 'Nick'

from PokerCalculator import Deck

def print_cards(cards):
    for card in cards:
        print(card.toString())

#sorts from highest value to lowest if reverse=True
def sort_cards(cards, reverse):
    sorted_cards = sorted(cards, key=lambda card: card.getHighValue(), reverse=reverse)
    return sorted_cards

#fills a given hand with high cards and returns the resulting 5 card hand... working
def calculate_high_cards(relevant_cards, remaining_cards) :
    _relevant_cards = relevant_cards
    _remaining_cards = remaining_cards
    number_of_cards = len(relevant_cards) + len(remaining_cards)
    assert(number_of_cards > 4)

    _remaining_cards.sort(key=lambda card: card.getHighValue(), reverse=True)

    while len(_relevant_cards) < 5 :
        _relevant_cards.append(_remaining_cards.pop(0))

    assert len(_relevant_cards) == 5
    assert len(_remaining_cards) == number_of_cards - len(_relevant_cards)

    return _relevant_cards

#returns true if two cards are within 1 value of each other
def get_connected(card1, card2):
    primary_diff = abs(card1.getHighValue() - card2.getHighValue())
    secondary_diff = None
    if(card1.getLowValue()):
        secondary_diff = abs(card1.getLowValue() - card2.getHighValue())
    if(card2.getLowValue()):
        secondary_diff = abs(card2.getLowValue() - card1.getHighValue())
    if(primary_diff == 1) or (secondary_diff == 1):
        return True

simple_straight_hand = [
    Deck.king_spades,
    Deck.queen_clubs,
    Deck.jack_spades,
    Deck.ten_spades,
    Deck.ace_hearts,
]

complex_straight_hand = [
    Deck.ace_hearts,
    Deck.king_spades,
    Deck.queen_clubs,
    Deck.jack_spades,
    Deck.ten_spades
]

multi_straight_hand = [
    Deck.eight_clubs,
    Deck.seven_spades,
    Deck.queen_clubs,
    Deck.jack_spades,
    Deck.ten_spades,
    Deck.nine_diamonds,
    Deck.six_hearts
]

from itertools import cycle


#licycle = cycle(li)
#nextelem = licycle.next()
#thiselem, nextelem = nextelem, licycle.next()

class CircleList:
    __items = []

    def __init__(self):
        print('init')

    def getItems(self):
        return self.__items

    def addItem(self, item):
        self.__items.append(item)

class CircleListItem:
    __card = None
    __previous = None
    __next = None

    def __init__(self, card, prev, next):
        __card = card
        __previous = prev
        __next = next



def check_for_straight(cards):
    assert len(cards) in range(5, 8)
    sorted_cards = sort_cards(cards, True)
    list_length = len(sorted_cards)

    relevant_cards = []

    #cl = CircleList()
    #for card in sorted_cards:
    #    cl.addItem(CircleListItem(card))


    for card1 in sorted_cards:
        temp_hand = [card1]

        for card2 in sorted_cards:
            if(card2 == card1):
                continue



        temp_hand = [card]
        if(get_connected(card, card.next)):
            print(card)
            print(card.next)
            temp_hand.append(card.next)
        else:
            continue


check_for_straight(simple_straight_hand)
#check_for_straight(complex_straight_hand)
#check_for_straight(multi_straight_hand)

