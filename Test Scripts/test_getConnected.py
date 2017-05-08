
import Data

def get_connected(card1, card2):
    primary_diff = abs(card1.getHighValue() - card2.getHighValue())
    secondary_diff = None
    if(card1.getLowValue()):
        secondary_diff = abs(card1.getLowValue() - card2.getHighValue())
    if(card2.getLowValue()):
        secondary_diff = abs(card2.getLowValue() - card1.getHighValue())
    if(primary_diff == 1) or (secondary_diff == 1):
        return True

if(get_connected(Data.ace_hearts, Data.king_spades)):
    print('yes1')

if(get_connected(Data.king_spades, Data.ace_hearts)):
    print('yes2')

if(get_connected(Data.two_spades, Data.ace_spades)):
    print('yes3')

if(get_connected(Data.ace_hearts, Data.two_spades)):
    print('yes4')

if(get_connected(Data.jack_spades, Data.eight_clubs)):
    print('no1')

def get_connected_collection(cards):
    length = len(cards)
    c5c4 = get_connected(cards[length-1], cards[length-2])
    c4c3 = get_connected(cards[length-2], cards[length-3])
    c3c2 = get_connected(cards[length-3], cards[length-4])
    c2c1 = get_connected(cards[length-4], cards[length-5])
    if(c5c4 and c4c3 and c3c2 and c2c1):
        return True
    else:
        return False