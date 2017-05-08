__author__ = 'Nick'

import Deck

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

def print_cards(cards):
    for card in cards:
        print(card.toString())

def sort_cards(cards):
    sorted_cards = sorted(cards, key=lambda card: card.getHighValue(), reverse=True)
    return sorted_cards

print('simple')
simple_sorted = sort_cards(simple_straight_hand)
print_cards(simple_sorted)
print('multi')
multi_sorted = sort_cards(multi_straight_hand)
print_cards(multi_sorted)
