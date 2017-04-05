__author__ = 'Nick'

from tkinter import *
import ViewTableBetting


class ViewTable:
    __parentView = None
    __betView = None

    def __init__(self, master):
        frame = Frame(master) #set height and width of Frame relative to MasterFrame
        frame.pack()
        self.button = Button(frame,
                             text="QUIT", fg="red",
                             command=quit)
        self.button.pack(side=LEFT)
        self.slogan = Button(frame,
                             text="Hello")
        self.slogan.pack(side=LEFT)

    def generateBetSlider(self):
        #if bet > stack, only draw Call or Fold
        #if bet < stack + min_raise > stack, only Allin or Call or Fold
        #else, all options are available
        print()

    def removeBetSlider(self):
        print()

root = Tk()
app = ViewTable(root)
root.mainloop()