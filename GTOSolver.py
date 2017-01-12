__author__ = 'Nick'




def getCombinations(n):
    x = 0
    sum = 0

    while(x < n):
        sum += (n-x-1) #+ (n-x-1)
        x += 1
        #print(sum)

    return sum

def getFlopCombinations(n):
    x = 0
    sum = (n*(n-1)*(n-2)) / (3*2*1)

    #while(x < n):
    #    sum += (n-x-1) + (n-x-2)
    #    x += 1
    #    print(sum)

    return sum

hand_combos = getCombinations(52)
turn_river_combos = getCombinations(45)
flop_combos_with_burns = getFlopCombinations(47)
flop_combos = getFlopCombinations(50)

#print(flop_combos)

def get_preflop_equity(hero, villain):
    #1 v 1 hands

def get_postflop_equity(hero, villain, board):


def get_equity_range(hero_array, villain_array):


    def compare_hands(hero_hand, villain_hand) :


    def compare_high_cards(hero_card, villain_card) :
        if(hero_card.value > villain_card.value):
            return True
        elif()




#def pushUnique(value):

#hands = {}

#call when started
#def generate_hands():
#    while(len(hands) < 1326):


#1326 - total hand combinations based on n=52
#19600 - total flop combinations based on n=50
#2,118,760 - total board combinations based on n=50

#paired hand (preflop) - 6/1326 == 0.45%
#unsuited hand like AQo (preflop) - 12/1326 == 0.905%
#suited hand like AQs (preflop) - 4/1326 == 0.302%


