__author__ = 'Nick'

import Data, HandHC

allCards = [
    Data.five_clubs,
    Data.four_spades,
    Data.jack_diamonds,
    Data.ace_hearts,
    Data.two_spades,
    Data.king_spades,
    Data.queen_clubs
]

madeHand1 = [
    Data.three_diamonds,
    Data.three_hearts,
    Data.three_spades
]

madeHand2 = [
    Data.three_hearts,
    Data.three_spades
]

madeHand3 = []



#fills a given hand with high cards and returns the resulting 5 card hand... working
def calculateHighCards(allCards, usedCards, length=5):
    remainingCards = []
    for c in allCards:
        if c not in usedCards:
            remainingCards.append(c)

    remainingCards.sort(key=lambda card: card.getHighValue(), reverse=True)
    additionalCards = length - len(usedCards)

    if additionalCards > 0:
        print(additionalCards)
        highCards = HandHC.HighCards(remainingCards[:additionalCards])
        return highCards
    else:
        print('This hand does not require any additional high cards.')
        #raise Exception('This hand does not require any additional high cards.')

final_hand = calculateHighCards(allCards, madeHand1)
print(final_hand)
print('-------------')
final_hand = calculateHighCards(allCards, madeHand2)
print(final_hand)
print('-------------')
final_hand = calculateHighCards(allCards, madeHand3)
print(final_hand)