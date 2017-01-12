__author__ = 'Nick'



class Quads:
    __quads = None
    __value = None
    __length = 4

    def __init__(self, quads):
        self.__quads = tuple(quads)
        self.__value = quads[0].value

        self.checkrep()

    def getLength(self):
        return self.__length

    @staticmethod
    def compare(self, quads1, quads2):
        if quads1.__value > quads2.__value:
            return quads1
        elif quads1.__value < quads2.__value:
            return quads2
        else:
            return 'Tied'

    def checkrep(self):
        assert len(self.__quads) == 4
        #also validate that the hand is actually quads