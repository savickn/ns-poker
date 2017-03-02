__author__ = 'Nick'

#returns true if two cards are within 1 value of each other
def isConnected(card1, card2):
    primary_diff = abs(card1.getHighValue() - card2.getHighValue())
    secondary_diff = None
    if(card1.getLowValue()):
        secondary_diff = abs(card1.getLowValue() - card2.getHighValue())
    if(card2.getLowValue()):
        secondary_diff = abs(card2.getLowValue() - card1.getHighValue())
    if(primary_diff == 1) or (secondary_diff == 1):
        return True

#uses 'isConnected' to check if all cards are connected
def isStraight(cards):
    length = len(cards)
    c5c4 = isConnected(cards[length-1], cards[length-2])
    c4c3 = isConnected(cards[length-2], cards[length-3])
    c3c2 = isConnected(cards[length-3], cards[length-4])
    c2c1 = isConnected(cards[length-4], cards[length-5])
    if(c5c4 and c4c3 and c3c2 and c2c1):
        return True
    else:
        return False

#fills a given hand with high cards and returns the resulting 5 card hand... working
def calculateHighCards(relevant_cards, remaining_cards) :
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

def printCards(cards):
    for card in cards:
        print(card.toString())

#sorts from highest value to lowest if reverse=True
def sortCards(cards, reverse):
    sorted_cards = sorted(cards, key=lambda card: card.getHighValue(), reverse=reverse)
    return sorted_cards