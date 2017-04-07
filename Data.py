__author__ = 'Nick'

import Card

ace_hearts = Card.Card('Ace', 'Hearts', 14, {'low_value': 1})
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
ace_spades = Card.Card('Ace', 'Spades', 14, {'low_value': 1})
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
ace_clubs = Card.Card('Ace', 'Clubs', 14, {'low_value': 1})
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
ace_diamonds = Card.Card('Ace', 'Diamonds', 14, {'low_value': 1})
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

cards = {}

cards['Hearts'] = [
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
    two_hearts
]

cards['Spades'] = [
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

cards['Clubs'] = [
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
    two_clubs
]

cards['Diamonds'] = [
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
    two_diamonds
]

cards['Ace'] = [
    ace_hearts,
    ace_clubs,
    ace_diamonds,
    ace_spades
]

cards['King'] = [
    king_clubs,
    king_spades,
    king_hearts,
    king_diamonds
]

cards['Queen'] = [
    queen_clubs,
    queen_spades,
    queen_hearts,
    queen_diamonds
]

cards['Jack'] = [
    jack_clubs,
    jack_spades,
    jack_diamonds,
    jack_hearts
]

cards['Ten'] = [
    ten_diamonds,
    ten_hearts,
    ten_spades,
    ten_clubs
]

cards['Nine'] = [
    nine_hearts,
    nine_spades,
    nine_diamonds,
    nine_clubs
]

cards['Eight'] = [
    eight_diamonds,
    eight_hearts,
    eight_clubs,
    eight_spades
]

cards['Seven'] = [
    seven_clubs,
    seven_diamonds,
    seven_hearts,
    seven_spades
]

cards['Six'] = [
    six_diamonds,
    six_spades,
    six_hearts,
    six_clubs
]

cards['Five'] = [
    five_clubs,
    five_spades,
    five_diamonds,
    five_hearts
]

cards['Four'] = [
    four_diamonds,
    four_clubs,
    four_spades,
    four_hearts
]

cards['Three'] = [
    three_hearts,
    three_diamonds,
    three_spades,
    three_clubs
]

cards['Two'] = [
    two_diamonds,
    two_spades,
    two_clubs,
    two_hearts
]

s = {}

s['1-5'] = {1, 2, 3, 4, 5}
s['2-6'] = {2, 3, 4, 5, 6}
s['3-7'] = {3, 4, 5, 6, 7}
s['4-8'] = {4, 5, 6, 7, 8}
s['5-9'] = {5, 6, 7, 8, 9}
s['6-T'] = {6, 7, 8, 9, 10}
s['7-J'] = {7, 8, 9, 10, 11}
s['8-Q'] = {8, 9, 10, 11, 12}
s['9-K'] = {9, 10, 11, 12, 13}
s['T-A'] = {10, 11, 12, 13, 14}


import HandStraight


straights = {}


straights['5-High'] = {'Ace', 'Two', 'Three', 'Four', 'Five'}
straights['6-High'] = {'Two', 'Three', 'Four', 'Five', 'Six'}
straights['7-High'] = {'Three', 'Four', 'Five', 'Six', 'Seven'}
straights['8-High'] = {'Four', 'Five', 'Six', 'Seven', 'Eight'}
straights['9-High'] = {'Five', 'Six', 'Seven', 'Eight', 'Nine'}
straights['T-High'] = {'Six', 'Seven', 'Eight', 'Nine', 'Ten'}
straights['J-High'] = {'Seven', 'Eight', 'Nine', 'Ten', 'Jack'}
straights['Q-High'] = {'Eight', 'Nine', 'Ten', 'Jack', 'Queen'}
straights['K-High'] = {'Nine', 'Ten', 'Jack', 'Queen', 'King'}
straights['A-High'] = {'Ten', 'Jack', 'Queen', 'King', 'Ace'}







