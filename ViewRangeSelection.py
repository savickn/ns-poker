__author__ = 'Nick'

from tkinter import *

class RangeView:
    __range = None #parent range
    __hands = None #hands to add or remove

    def __init__(self, range):
        self.__range = range
        #draw everything


    #event handlers when clicking on particular hand
    def onSelect(self, hands):
        self.__range.addHandsToRange(hands)

    def onUnSelect(self, hands):
        self.__range.removeHandsFromRange(hands)

