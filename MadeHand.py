__author__ = 'Nick'

class MadeHand:
    __hands = None
    __length = None

    def __init__(self, hands):
        self.__hands = tuple(hands)
        for hand in hands:
            self.__length += hand.getLength()

        self.checkrep()

    def checkrep(self):
        assert self.__length == 5