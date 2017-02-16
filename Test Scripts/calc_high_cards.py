__author__ = 'Nick'

from PokerCalculator import Deck

relevant_cards1 = [
    Deck.three_diamonds,
    Deck.three_hearts,
    Deck.three_spades
]

remaining_cards1 = [
    Deck.five_clubs,
    Deck.jack_diamonds,
    Deck.ace_hearts,
    Deck.two_spades
]

relevant_cards2 = []
remaining_cards2 = [
    Deck.five_clubs,
    Deck.four_spades,
    Deck.jack_diamonds,
    Deck.ace_hearts,
    Deck.two_spades,
    Deck.king_spades,
    Deck.queen_clubs
]

relevant_cards3 = []
remaining_cards3 = [
    Deck.five_clubs,
    Deck.four_spades,
    Deck.jack_diamonds,
    Deck.ace_hearts
]

#utility method for printing string representation of a list of cards
def print_cards(cards):
    for card in cards:
        print(card.toString())

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

final_hand = calculate_high_cards(relevant_cards1, remaining_cards1)
print_cards(final_hand)
print('-------------')
final_hand = calculate_high_cards(relevant_cards2, remaining_cards2)
print_cards(final_hand)
print('-------------')
final_hand = calculate_high_cards(relevant_cards3, remaining_cards3)
print_cards(final_hand)