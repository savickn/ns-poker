__author__ = 'Nick'

import HandBest, Data, HandTrips, HandHC, HandPreflop


pf = HandPreflop.HoldemHand([Data.ace_clubs, Data.ace_spades])
t = HandTrips.Trips([Data.ace_clubs, Data.ace_spades, Data.ace_diamonds])
hc = HandHC.HighCards([Data.king_spades, Data.four_spades])

print(pf)
print(t)
print(hc)

hb = HandBest.HandBest(pf, t, hc)
print(hb)
