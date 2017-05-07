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

#Helper function for extracting the best possible flush
def extractBestFlush(cards):
    cards.sort(key=lambda card: card.getHighValue(), reverse=True)
    return HandFlush.Flush(cards[:5])

def analyzeSuit(cards, checkDraws):
    if len(cards) >= 5:
        f = extractBestFlush(cards)
    elif len(cards) == 4 and checkDraws:
        __flushDraws.append()
    elif len(cards) == 3 and checkDraws:
        __backdoorFDs.append()

#extracts all possible flushes from availableCards (required to calc possible straight_flushes)
def analyzeFlushes(cards, checkDraws=False):
    assert len(cards) in range(5, 8)
    flushes = []
    flushDraws = []
    flushBackdoorDraws = []

    spades = []
    clubs = []
    diamonds = []
    hearts = []

    for card in cards:
        if(card.getSuit() == 'Spades'):
            spades.append(card)
        elif(card.getSuit() == 'Hearts'):
            hearts.append(card)
        elif(card.getSuit() == 'Clubs'):
            clubs.append(card)
        elif(card.getSuit() == 'Diamonds'):
            diamonds.append(card)
        else:
            raise Exception('This card has an invalid suit.')

    analyzeSuit(spades, checkDraws)
    analyzeSuit(clubs, checkDraws)
    analyzeSuit(diamonds, checkDraws)
    analyzeSuit(hearts, checkDraws)

flush = analyzeFlushes(flush_hand)
print(flush)
print('-----------')
no_flush = analyzeFlushes(no_flush_hand)
print(no_flush)
