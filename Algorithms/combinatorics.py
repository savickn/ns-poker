__author__ = 'Nick'

#returns total number of unique Combos (e.g. flop has 3 perHand, board has 5 perHand, omaha has 4 perHand, holdem has 2 perHand)
def getCombos(totalCards, perHand):
    it = 0
    den = 1
    num = 1

    #used to set the numerator and denominator
    while it < perHand:
        den *= (perHand - it)
        num *= (totalCards - it)
        it += 1

    combos = num / den
    print(combos)
    return combos

#Omaha hands
getCombos(52, 4)

#Holdem hands
getCombos(52, 2)

#Flop combos
getCombos(50, 3)


#turn_river_combos = getCombinations(45)
#flop_combos_with_burns = GtoSolver.getFlopCombinations(47)


#1326 - total hand combinations based on n=52
#19600 - total flop combinations based on n=50
#2,118,760 - total board combinations based on n=50

#paired hand (preflop) - 6/1326 == 0.45%
#unsuited hand like AQo (preflop) - 12/1326 == 0.905%
#suited hand like AQs (preflop) - 4/1326 == 0.302%


#def getHoldemCombos(n):
#    x = 0
#    sum = 0
#    while(x < n):
#        sum += (n-x-1)
#        x += 1
#    return sum

#def getFlopCombos(n):
#    x = 0
#    sum = (n*(n-1)*(n-2)) / (3*2*1)
#    while(x < n):
#       sum += (n-x-1) + (n-x-2)
#       x += 1
#       print(sum)
#    return sum