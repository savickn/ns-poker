__author__ = 'Nick'

#for betting and raising, overlaid on TableView

from tkinter import *

#top = Tk()
# Code to add widgets will go here...

#used for betting/calling/folding
#frame = Frame()
#frame.pack()

#top.mainloop()

#class ViewTableBetting:
#    def __init__(self, master):



class ViewTableBetting:
  def __init__(self, master):
    frame = Frame(master, anchor=SE) #set height and width of Frame relative to MasterFrame
    frame.pack()
    self.button = Button(frame,
                         text="QUIT", fg="red",
                         command=quit)
    self.button.pack(side=LEFT)
    self.slogan = Button(frame,
                         text="Hello",
                         command=self.write_slogan)
    self.slogan.pack(side=LEFT)
  def write_slogan(self):
    print("Tkinter is easy to use!")

root = Tk()
app = ViewTableBetting(root)
root.mainloop()