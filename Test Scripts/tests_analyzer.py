__author__ = 'Nick'

import Data, Board, HandPreflop, HandBest, HandAnalyzer
import HandPair, HandTP, HandTrips, HandStraight, HandFlush, HandFH, HandQuads, HandSF, HandHC


hand = HandPreflop.HoldemHand(
    [Data.ace_spades,
    Data.seven_spades])

hand2 = HandPreflop.HoldemHand(
    [Data.ace_clubs,
    Data.king_spades])

#High-Card Hand Tests

#high cards
board1 = Board.Board(
    Data.king_clubs,
    Data.six_diamonds,
    Data.five_spades,
    Data.jack_clubs,
    Data.ten_diamonds)

#Pair-Type Hand Tests

#Hand + Board pair
board2 = Board.Board(
    Data.ace_hearts,
    Data.five_spades,
    Data.four_spades,
    Data.three_hearts,
    Data.ten_hearts)

#Board only pair
board3 = Board.Board(
    Data.five_clubs,
    Data.five_spades,
    Data.four_spades,
    Data.three_hearts,
    Data.ten_hearts)

#two pair
board4 = Board.Board(
    Data.king_hearts,
    Data.five_clubs,
    Data.seven_diamonds,
    Data.ten_hearts,
    Data.ten_clubs)

#trips
board5 = Board.Board(
    Data.ace_hearts,
    Data.ace_clubs,
    Data.five_spades,
    Data.four_spades,
    Data.three_hearts)

#Board-only full house
board6 = Board.Board(
    Data.five_hearts,
    Data.five_clubs,
    Data.ten_diamonds,
    Data.ten_hearts,
    Data.ten_clubs)

#double-trips full house
board7 = Board.Board(
    Data.ace_hearts,
    Data.ace_clubs,
    Data.ten_diamonds,
    Data.ten_hearts,
    Data.ten_clubs)

#quads
board8 = Board.Board(
    Data.ace_hearts,
    Data.ace_clubs,
    Data.ace_diamonds,
    Data.ten_hearts,
    Data.ten_clubs)

#Flush-Type Hand Tests

#flush
board9 = Board.Board(
    Data.king_spades,
    Data.five_spades,
    Data.six_spades,
    Data.ten_spades,
    Data.jack_spades)

#Straight-Type Hand Tests

#Ace-high straight
board10 = Board.Board(
    Data.king_spades,
    Data.jack_clubs,
    Data.queen_diamonds,
    Data.ten_hearts,
    Data.jack_spades)

#Ace-low straight
board11 = Board.Board(
    Data.two_spades,
    Data.three_clubs,
    Data.four_diamonds,
    Data.five_hearts,
    Data.jack_spades)

#middle card straight
board12 = Board.Board(
    Data.six_spades,
    Data.three_clubs,
    Data.four_diamonds,
    Data.five_hearts,
    Data.jack_spades)

#straight flush
board13 = Board.Board(
    Data.six_spades,
    Data.five_spades,
    Data.four_spades,
    Data.three_spades,
    Data.two_spades)


printHighCards = False
printPairedHands = False
printFlushes = False
printStraights = False

ha1 = HandAnalyzer.HandAnalyzer(hand, board1, printHighCards)
assert isinstance(ha1.getBestHand().getPrimary(), HandHC.HighCards)

ha2 = HandAnalyzer.HandAnalyzer(hand, board2, printPairedHands)
assert isinstance(ha2.getBestHand().getPrimary(), HandPair.Pair)

ha3 = HandAnalyzer.HandAnalyzer(hand, board3, printPairedHands)
assert isinstance(ha3.getBestHand().getPrimary(), HandPair.Pair)

ha4 = HandAnalyzer.HandAnalyzer(hand, board4, printPairedHands)
assert isinstance(ha4.getBestHand().getPrimary(), HandTP.TwoPair)

ha5 = HandAnalyzer.HandAnalyzer(hand, board5, printPairedHands)
assert isinstance(ha5.getBestHand().getPrimary(), HandTrips.Trips)

ha6 = HandAnalyzer.HandAnalyzer(hand, board6, printPairedHands)
assert isinstance(ha6.getBestHand().getPrimary(), HandFH.FullHouse)

ha7 = HandAnalyzer.HandAnalyzer(hand, board7, printPairedHands)
assert isinstance(ha7.getBestHand().getPrimary(), HandFH.FullHouse)

ha8 = HandAnalyzer.HandAnalyzer(hand, board8, printPairedHands)
assert isinstance(ha8.getBestHand().getPrimary(), HandQuads.Quads)

ha9 = HandAnalyzer.HandAnalyzer(hand, board9, printFlushes)
assert isinstance(ha9.getBestHand().getPrimary(), HandFlush.Flush)

ha10 = HandAnalyzer.HandAnalyzer(hand, board10, printStraights)
assert isinstance(ha10.getBestHand().getPrimary(), HandStraight.Straight)

ha11 = HandAnalyzer.HandAnalyzer(hand, board11, printStraights)
assert isinstance(ha11.getBestHand().getPrimary(), HandStraight.Straight)

ha12 = HandAnalyzer.HandAnalyzer(hand, board12, printStraights)
assert isinstance(ha12.getBestHand().getPrimary(), HandStraight.Straight)

ha13 = HandAnalyzer.HandAnalyzer(hand, board13, printStraights)
assert isinstance(ha13.getBestHand().getPrimary(), HandSF.StraightFlush)


