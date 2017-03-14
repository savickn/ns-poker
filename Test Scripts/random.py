__author__ = 'Nick'







    #calculates remaining cards using symmetrical difference
    #remaining_cards = set(relevant_cards) ^ set(initial_cards)
    #remaining_cards = list(remaining_cards)
    #best_hand = calculate_high_cards(relevant_cards, remaining_cards)

    ############### Individual Hand Checks ####################

    #def hasStraightFlush(self):
    #    sf = None
    #    for hand in self.__flushes:
    #        if Helpers.isStraight(hand):
    #            return

    # #def hasQuads(self):
    #     sf = None
    #     for hand in self.__flushes:
    #         if Helpers.isStraight(hand):
    #             self.__bestHand = hand
    #             return
    #
    # def hasFullHouse(self):
    #     sf = None
    #     for hand in self.__flushes:
    #         if Helpers.isStraight(hand):
    #             self.__bestHand = hand
    #             return
    #
    # def hasStraight(self):
    #     sf = None
    #     for hand in self.__flushes:
    #         if Helpers.isStraight(hand):
    #             self.__bestHand = hand
    #             return
    #
    # def hasFlush(self):
    #     print()
    #
    # def hasTrips(self):
    #     print()
    #
    # def hasTwoPair(self):
    #     print()
    #
    # def hasPair(self):
    #     print()

    # def calculateBestHand(self):
    #
    #     if self.hasStraightFlush():
    #         self.__bestHand = self.__straightFlushes[0]
    #
    #     if self.hasQuads():
    #         self.__bestHand = self.__quads[0]
    #
    #     if self.hasFullHouse():
    #         return self.__bestHand
    #
    #     if self.hasFlush():
    #         return self.__bestHand
    #
    #     if self.hasStraight():
    #         return self.__bestHand
    #
    #     if self.hasTrips():
    #         return self.__bestHand
    #
    #     if self.hasTwoPair():
    #         return self.__bestHand
    #
    #     if self.hasPair():
    #         return self.__bestHand

# class Card_Type(Enum):
#     ACE_LO = 1
#     TWO = 2
#     THREE = 3
#     FOUR = 4
#     FIVE = 5
#     SIX = 6
#     SEVEN = 7
#     EIGHT = 8
#     NINE = 9
#     TEN = 10
#     JACK = 11
#     QUEEN = 12
#     KING = 13
#     ACE_HIGH = 14
#
# class Card_Suit(Enum):
#     CLUBS = 1
#     HEARTS = 2
#     DIAMONDS = 3
#     SPADES = 4



#pa1 = [
#    Deck.two_hearts,
#    Deck.two_spades
#]

#pa2 = [
#    Deck.five_clubs,
#    Deck.five_spades
#]

#pair1 = Pair(pa1, pa1[0].getHighValue())
#pair2 = Pair(pa2, pa2[0].getHighValue())

#winner = Pair.compare(pair1, pair2)
#print(winner.toString())
