__author__ = 'Nick'

import Data, HandFlush, DrawFlush, DrawBackdoorFlush

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

fd = [
    Data.ace_diamonds,
    Data.king_diamonds,
    Data.ten_diamonds,
    Data.four_diamonds
]



#Helper function for extracting the best possible flush
def extractBestFlush(cards):
    cards.sort(key=lambda card: card.getHighValue(), reverse=True)
    return HandFlush.Flush(cards[:5])

def analyzeSuit(cards, data, checkDraws):
    if len(cards) >= 5:
        f = extractBestFlush(cards)
        data['flushes'].append(f)
    elif len(cards) == 4 and checkDraws:
        data['draws'].append(DrawFlush.FlushDraw(cards, cards[0].getSuit()))
    elif len(cards) == 3 and checkDraws:
        data['backdoorDraws'].append(DrawBackdoorFlush.BackdoorFlushDraw(cards, cards[0].getSuit()))
    return data

#extracts all possible flushes from availableCards (required to calc possible straight_flushes)
def analyzeFlushes(cards, checkDraws=False):
    data = {
        'flushes': [],
        'draws': [],
        'backdoorDraws': []
    }

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

    data = analyzeSuit(spades, data, checkDraws)
    data = analyzeSuit(clubs, data, checkDraws)
    data = analyzeSuit(diamonds, data, checkDraws)
    data = analyzeSuit(hearts, data, checkDraws)

    for f in data['flushes']:
        print(f)
    for fd in data['draws']:
        print(fd)
    for bfd in data['backdoorDraws']:
        print(bfd)

#analyzeFlushes(flush_hand)
#analyzeFlushes(no_flush_hand, True)
analyzeFlushes(fd, True)

