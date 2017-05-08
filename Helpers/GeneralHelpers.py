__author__ = 'Nick'

#sorts based on a card's highValue field (highest value to lowest if reverse=True and vice versa), WORKING
def highSort(cards, reverse):
    sorted_cards = sorted(cards, key=lambda card: card.getHighValue(), reverse=reverse)
    return sorted_cards

#sorts based on a card's lowValue field, WORKING
def lowSort(cards, reverse):
    sorted_cards = sorted(cards, key=lambda card: card.getLowValue(), reverse=reverse)
    return sorted_cards

#checks if a Hand (e.g. HandQuads or HandFlush) is in a collection (based on Hand.__id), WORKING
def inCollection(hand, collection):
    for h in collection:
        if h == hand:
            return True
    return False