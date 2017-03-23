__author__ = 'Nick'

import HandPreflop, Data
import random

default = []


preflopHands = {}

class Deck:

    def __init__(self, deadCards=default, generateHands=False):
        self.__cards = Data.deck if len(deadCards) == 0 else list(set(Data.deck) - set(deadCards))
        self.__length = len(self.__cards)
        self.checkRep()

        if generateHands:
            self.generateHoldemHandCombos() #used to populate 'preflopHands'

    def shuffleDeck(self):
        self.__cards = Deck.shuffle(self.__cards)

    @staticmethod
    def shuffle(cards):
        ary = cards
        a=len(ary)
        b=a-1
        for d in range(b,0,-1):
          e=random.randint(0,d)
          if e == d:
                continue
          ary[d],ary[e]=ary[e],ary[d]
        return ary

    #used to reset the Deck to a default state
    def resetDeck(self):
        self.__cards = Data.deck

    #used to remove dead cards
    def removeDeadCards(self, deadCards):
        self.__cards = list(set(self.__cards) - set(deadCards))

    #used to retrieve the top card (either for Dealing a Hand or Burning)
    def getTopCard(self):
        card =  self.__cards.pop(0)
        self.__length = len(self.__cards)
        return card

    ############# HAND COMBINATORICS #################

    def generateHoldemHandCombos(self, toPrint=False):
        processed_cards = []

        hands = []
        pairedHands = []
        suitedHands = []
        offsuitHands = []

        for card1 in self.__cards:
            for card2 in self.__cards:
                if (card1 is not card2) and (card2 not in processed_cards):
                    pHand = HandPreflop.HoldemHand([card1, card2])
                    if pHand not in hands:
                        hands.append(pHand)
            processed_cards.append(card1)

        for hand in hands:
            #adds PreflopHand to general category (e.g. Paired Hand vs. Suited Hand)
            #if hand.isPaired():
            #    pairedHands.append(hand)
            #elif hand.isSuited():
            #    suitedHands.append(hand)
            #else:
            #    offsuitHands.append(hand)

            #adds PreflopHand to specific category (AKs vs. AQo)
            if hand.getInitials() in preflopHands.keys():
                preflopHands[hand.getInitials()].append(hand)
            else:
                preflopHands[hand.getInitials()] = [hand]

        if toPrint:
            print('##### HAND TYPES #####')
            for key, value in preflopHands.items():
                length = len(preflopHands[key])
                print('{key}-{length}'.format(key=key, length=length))

            print('##### COMBINATIONS #####')
            print(len(suitedHands)) #should be 312
            print(len(pairedHands)) #should be 78
            print(len(offsuitHands)) #should be 936
            print(len(hands)) #should be 1,326

    ############## UTILITY METHODS ##############

    def toString(self):
        str = ''
        for c in self.__cards:
            str += '{card} \n'.format(card=c.toString())
        return str

    def printAsString(self):
        print('##### DECK COUNT #####')
        print(self.__length)
        print('##### DECK #####')
        print(self.toString())

    def checkRep(self):
        assert self.__length <= 52 and self.__length >= 0

#d = Deck([Data.ace_spades, Data.three_spades])
#d.generateHoldemHandCombos(True)




#d.generateOmahaHandCombos()

#d = Deck()
#c = d.getTopCard()
#print(c.getState())
#c.setState(False)
#print(c.getState())

#d = Deck()
#c = d.getTopCard()
#print(c.getState())


#def generateOmahaHandCombos(self):
#        processed_cards = []
#        hands = []
#        for card1 in self.__cards:
#            for card2 in self.__cards:
#                for card3 in self.__cards:
#                    for card4 in self.__cards:
#                        if (card1 not in [card2, card3, card4]) and (card2 not in [card3, card4]) and (card3 is not card4):
#                            hand = PreflopHand.OmahaHand(card1, card2, card3, card4)
#                            if (hand not in hands):
#                                hands.append(hand)
#        print(len(hands))

#def refreshLength(self):
#        self.__length = len(self.__cards)
#        print('refresh hand combos')