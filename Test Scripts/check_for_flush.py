__author__ = 'Nick'

import Data, Helpers, HandFlush

flush_hand = [
    Data.ace_hearts,
    Data.king_hearts,
    Data.queen_hearts,
    Data.ten_hearts,
    Data.nine_hearts,
    Data.eight_hearts,
    Data.six_hearts
]

no_flush_hand = [
    Data.ace_hearts,
    Data.king_spades,
    Data.queen_diamonds,
    Data.ten_hearts,
    Data.nine_spades,
    Data.eight_diamonds,
    Data.six_hearts
]

def analyzeFlushes(cards):
    assert len(cards) in range(5, 8)
    flushes = []
    flushDraws = []
    flushBackdoorDraws = []

    spades = []
    clubs = []
    diamonds = []
    hearts = []

    for c in cards:
        if(c.getSuit() == 'Spades'):
            spades.append(c)
        elif(c.getSuit() == 'Hearts'):
            hearts.append(c)
        elif(c.getSuit() == 'Clubs'):
            clubs.append(c)
        elif(c.getSuit() == 'Diamonds'):
            diamonds.append(c)
        else:
            raise Exception('This card has an invalid suit.')

    if(len(spades) >= 5):
        flushes.append(HandFlush.Flush(spades))
    elif(len(spades) == 4 and len(cards) < 7):
        flushDraws.append(s)

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
