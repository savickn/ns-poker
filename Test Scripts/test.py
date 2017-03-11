__author__ = 'Nick'

import Deck


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


hand = [
    Deck.ace_hearts,
    Deck.ace_spades,
    Deck.king_spades,
    Deck.eight_diamonds,
    Deck.seven_clubs,
    Deck.two_diamonds,
    Deck.four_spades
]

for card in hand[1:6]:
    print(card.toString())

