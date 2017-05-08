__author__ = 'Nick'

#helper for checking if all elements in a collection have the same suit
def isSameSuit(cards):
    suit = cards[0].getSuit()
    for c in cards:
        if c.getSuit() != suit:
            return False
    return True

#checks for Flush
def isFlush(cards):
    return True if len(cards) >= 5 and isSameSuit(cards) else False

#checks for Flush Draw
def isFlushDraw(cards):
    return True if len(cards) == 4 and isSameSuit(cards) else False

#checks for Backdoor Flush Draw
def isBackdoorFlushDraw(cards):
    return True if len(cards) == 3 and isSameSuit(cards) else False
