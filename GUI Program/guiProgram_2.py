#GUI Programming - 2 (Buttons)

from tkinter import *
'''Don't need to keep uisng tkinter keyword, directly call the method'''

w = Tk()
w.geometry("200x50")

w.title("Button work!")

btn = Button(w, text="I don't work!")

btn.pack()

mainloop()
