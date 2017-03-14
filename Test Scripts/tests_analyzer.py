__author__ = 'Nick'

import Deck, Board, HandPreflop, HandBest, HandAnalyzer
import HandPair, HandTP, HandTrips, HandStraight, HandFlush, HandFH, HandQuads, HandSF, HandHC


hand = HandPreflop.HoldemHand(
    Deck.ace_spades,
    Deck.seven_spades)

hand2 = HandPreflop.HoldemHand(
    Deck.ace_clubs,
    Deck.king_spades)

#High-Card Hand Tests

#high cards
board1 = Board.Board(
    Deck.king_clubs,
    Deck.six_diamonds,
    Deck.five_spades,
    Deck.jack_clubs,
    Deck.ten_diamonds)

#Pair-Type Hand Tests

#Hand + Board pair
board2 = Board.Board(
    Deck.ace_hearts,
    Deck.five_spades,
    Deck.four_spades,
    Deck.three_hearts,
    Deck.ten_hearts)

#Board only pair
board3 = Board.Board(
    Deck.five_clubs,
    Deck.five_spades,
    Deck.four_spades,
    Deck.three_hearts,
    Deck.ten_hearts)

#two pair
board4 = Board.Board(
    Deck.king_hearts,
    Deck.five_clubs,
    Deck.seven_diamonds,
    Deck.ten_hearts,
    Deck.ten_clubs)

#trips
board5 = Board.Board(
    Deck.ace_hearts,
    Deck.ace_clubs,
    Deck.five_spades,
    Deck.four_spades,
    Deck.three_hearts)

#Board-only full house
board6 = Board.Board(
    Deck.five_hearts,
    Deck.five_clubs,
    Deck.ten_diamonds,
    Deck.ten_hearts,
    Deck.ten_clubs)

#double-trips full house
board7 = Board.Board(
    Deck.ace_hearts,
    Deck.ace_clubs,
    Deck.ten_diamonds,
    Deck.ten_hearts,
    Deck.ten_clubs)

#quads
board8 = Board.Board(
    Deck.ace_hearts,
    Deck.ace_clubs,
    Deck.ace_diamonds,
    Deck.ten_hearts,
    Deck.ten_clubs)

#Flush-Type Hand Tests

#flush
board9 = Board.Board(
    Deck.king_spades,
    Deck.five_spades,
    Deck.six_spades,
    Deck.ten_spades,
    Deck.jack_spades)

#Straight-Type Hand Tests

#Ace-high straight
board10 = Board.Board(
    Deck.king_spades,
    Deck.jack_clubs,
    Deck.queen_diamonds,
    Deck.ten_hearts,
    Deck.jack_spades)

#Ace-low straight
board11 = Board.Board(
    Deck.two_spades,
    Deck.three_clubs,
    Deck.four_diamonds,
    Deck.five_hearts,
    Deck.jack_spades)

#straight with A-high
board12 = Board.Board(
    Deck.six_spades,
    Deck.three_clubs,
    Deck.four_diamonds,
    Deck.five_hearts,
    Deck.jack_spades)

#straight flush
board13 = Board.Board(
    Deck.six_spades,
    Deck.five_spades,
    Deck.four_spades,
    Deck.three_spades,
    Deck.two_spades)


toPrint = False

ha1 = HandAnalyzer.HandAnalyzer(hand, board1, toPrint)
assert isinstance(ha1.getBestHand().getPrimary(), HandHC.HighCards)

ha2 = HandAnalyzer.HandAnalyzer(hand, board2, toPrint)
assert isinstance(ha2.getBestHand().getPrimary(), HandPair.Pair)

ha3 = HandAnalyzer.HandAnalyzer(hand, board3, toPrint)
assert isinstance(ha3.getBestHand().getPrimary(), HandPair.Pair)

ha4 = HandAnalyzer.HandAnalyzer(hand, board4, toPrint)
assert isinstance(ha4.getBestHand().getPrimary(), HandTP.TwoPair)

ha5 = HandAnalyzer.HandAnalyzer(hand, board5, toPrint)
assert isinstance(ha5.getBestHand().getPrimary(), HandTrips.Trips)

ha6 = HandAnalyzer.HandAnalyzer(hand, board6, toPrint)
assert isinstance(ha6.getBestHand().getPrimary(), HandFH.FullHouse)

ha7 = HandAnalyzer.HandAnalyzer(hand, board7, toPrint)
assert isinstance(ha7.getBestHand().getPrimary(), HandFH.FullHouse)

ha8 = HandAnalyzer.HandAnalyzer(hand, board8, toPrint)
assert isinstance(ha8.getBestHand().getPrimary(), HandQuads.Quads)

ha9 = HandAnalyzer.HandAnalyzer(hand, board9, toPrint)
assert isinstance(ha9.getBestHand().getPrimary(), HandFlush.Flush)

ha10 = HandAnalyzer.HandAnalyzer(hand, board10, True)
assert isinstance(ha10.getBestHand().getPrimary(), HandStraight.Straight)

ha11 = HandAnalyzer.HandAnalyzer(hand, board11, True)
assert isinstance(ha11.getBestHand().getPrimary(), HandStraight.Straight)

ha12 = HandAnalyzer.HandAnalyzer(hand, board12, True)
assert isinstance(ha12.getBestHand().getPrimary(), HandStraight.Straight)



