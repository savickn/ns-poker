__author__ = 'Nick'

from PokerCalculator import Deck

trips_hand_seven = [
    Deck.three_diamonds,
    Deck.three_hearts,
    Deck.three_spades,
    Deck.five_clubs,
    Deck.jack_diamonds,
    Deck.ace_clubs,
    Deck.king_diamonds
]

no_trips_hand = [
    Deck.five_clubs,
    Deck.jack_diamonds,
    Deck.ace_hearts,
    Deck.two_spades,
    Deck.ace_spades
]

double_trips_hand = [
    Deck.three_diamonds,
    Deck.three_hearts,
    Deck.three_spades,
    Deck.four_diamonds,
    Deck.four_hearts,
    Deck.four_spades,
    Deck.five_spades
]

def print_cards(cards):
    for card in cards:
        print(card.toString())

def print_best_hand(cards, type):
    print('The following cards make {type}: {card1}, {card2}, {card3}, {card4}, {card5}'.format(type=type, card1=cards[0].toString(),
                                                                                                card2=cards[1].toString(), card3=cards[2].toString(),
                                                                                                card4=cards[3].toString(), card5=cards[4].toString()))

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

#sets Class.__best_hand and returns True if __best_hand was updated, else returns False if no changes were made.
def check_for_trips(cards):
    assert len(cards) >= 5

    initial_cards = cards
    relevant_cards = []

    for parent_card in cards:
        if parent_card in relevant_cards:
            continue

        temp_hand = [parent_card]

        for card in cards:
            if card == parent_card or card in relevant_cards:
                continue
            if (parent_card.getHighValue() == card.getHighValue()):
                print('{parent_card} matched {card}. Therefore, {card} was added to temp_hand.'.format(card=card.toString(),
                                                                                                       parent_card=parent_card.toString()))
                temp_hand.append(card)

        if len(temp_hand) == 3:
            print('{parent_card} makes trips.'.format(parent_card=parent_card.toString()))
            relevant_cards.extend(temp_hand)

        else:
            print('{parent_card} does not make trips.'.format(parent_card=parent_card.toString()))

    #at this point, relevant_cards has either 0 or 3 or 6 values
    assert len(relevant_cards) in [0, 3, 6]

    if len(relevant_cards) == 3:
        #calculates remaining cards using symmetrical difference
        remaining_cards = set(relevant_cards) ^ set(initial_cards)
        remaining_cards = list(remaining_cards)

        print('remaining')
        print_cards(remaining_cards)
        print('relevant')
        print_cards(relevant_cards)

        best_hand = calculate_high_cards(relevant_cards, remaining_cards)

        print_best_hand(best_hand, 'Trips')

    #elif len(relevant_cards) == 6:
        #handle 6 cards, doesnt matter as long as Full House catches this possibility

    else:
        print('This hand does not contain trips.')

print('trips_hand')
check_for_trips(trips_hand_seven)
print('no_trips_hand')
check_for_trips(no_trips_hand)
print('double trips hand')
check_for_trips(double_trips_hand)
