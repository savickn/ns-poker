__author__ = 'Nick'

from PokerCalculator import Deck

flush_hand = [
    Deck.ace_hearts,
    Deck.king_hearts,
    Deck.queen_hearts,
    Deck.ten_hearts,
    Deck.nine_hearts,
    Deck.eight_hearts,
    Deck.six_hearts
]

no_flush_hand = [
    Deck.ace_hearts,
    Deck.king_spades,
    Deck.queen_diamonds,
    Deck.ten_hearts,
    Deck.nine_spades,
    Deck.eight_diamonds,
    Deck.six_hearts
]

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

def print_cards(cards):
    for card in cards:
        print(card.toString())

def check_for_flush(cards):
    assert len(cards) in range(5, 8)
    made_hand = []

    spades = []
    clubs = []
    diamonds = []
    hearts = []

    for parent_card in cards:
        if(parent_card.getSuit() == 'Spades'):
            spades.append(parent_card)
        elif(parent_card.getSuit() == 'Hearts'):
            hearts.append(parent_card)
        elif(parent_card.getSuit() == 'Clubs'):
            clubs.append(parent_card)
        elif(parent_card.getSuit() == 'Diamonds'):
            diamonds.append(parent_card)
        else:
            raise Exception('This card has an invalid suit.')

    if(len(spades) >= 5):
        made_hand = calculate_high_cards([], spades)
    elif(len(clubs) >= 5):
        made_hand = calculate_high_cards([], clubs)
    elif(len(hearts) >= 5):
        made_hand = calculate_high_cards([], hearts)
    elif(len(diamonds) >= 5 ):
        made_hand = calculate_high_cards([], diamonds)
    else:
        print('This hand does not make a flush.')

    return made_hand

flush = check_for_flush(flush_hand)
print_cards(flush)
print('-----------')
no_flush = check_for_flush(no_flush_hand)
print_cards(no_flush)