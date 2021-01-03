#GUI Program in Python 4 - CheckButtons

from tkinter import *

top = Tk()

ck1 = Checkbutton(top, text="Kivy").pack()
ck2 = Checkbutton(top, text = "wxPython").pack()

top.mainloop()
