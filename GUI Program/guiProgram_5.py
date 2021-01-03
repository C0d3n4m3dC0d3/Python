#GUI Program in Python 5 - CheckButtons with grid()
'''grid() method provides matrix like structues for displaying components'''

from tkinter import *

top = Tk()

ck1 = Checkbutton(top, text="Kivy").grid(row=0, column = 0, sticky="W")
ck2 = Checkbutton(top, text = "wxPython").grid(row=1, column = 0, sticky="W")

top.mainloop()
