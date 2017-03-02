__author__ = 'Nick'



#used to determine top/bottom 10% of range based on board
class BoardAnalyzer:
    __board = None
    __range = None

    def __init__(self, board, range):
        self.__board = board
        self.__range = range

