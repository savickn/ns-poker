__author__ = 'Nick'

from itertools import cycle
import Data


hand = [
    Data.ace_hearts,
    Data.ace_spades,
    Data.king_spades,
    Data.eight_diamonds,
    Data.seven_clubs,
    Data.two_diamonds,
    Data.four_spades
]

for card in hand[1:6]:
    print(card.toString())

#licycle = cycle(li)
#nextelem = licycle.next()
#thiselem, nextelem = nextelem, licycle.next()

class CircleList:
    __items = []

    def __init__(self):
        print('init')

    def getItems(self):
        return self.__items

    def addItem(self, item):
        self.__items.append(item)

class CircleListItem:
    __card = None
    __previous = None
    __next = None

    def __init__(self, card, prev, next):
        __card = card
        __previous = prev
        __next = next


class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):
    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

#print(x.Name())
#print(y.GetEmployee())


def calculate_high_cards(relevant_cards, remaining_cards) :
    _relevant_cards = relevant_cards
    _remaining_cards = remaining_cards
    number_of_cards = len(relevant_cards) + len(remaining_cards)
    assert(number_of_cards > 4)

    _remaining_cards.sort(key=lambda card: card.getHighValue(), reverse=True)

    while len(_relevant_cards) < 5 :
        _relevant_cards.append(_remaining_cards.pop(0))

    assert len(_relevant_cards) == 5
    assert len(_remaining_cards) == number_of_cards - len(_relevant_cards)

    return _relevant_cards
