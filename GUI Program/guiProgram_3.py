#GUI Programming - 3 (Frames)

from tkinter import *

w = Tk()
w.geometry("600x300")

w.title("Frames!")

t_frame = Frame(w).pack(side="top")
b_frame = Frame(w).pack(side="bottom")

lblTop1 = Label(t_frame, text="Top Frame, Label 1!", fg="yellow", bg="black").pack(side="top")
lblTop2 = Label(t_frame, text="Yo! Top Frame, Label 2!",fg="black", bg ="lightblue").pack(side="bottom")

btnBtm1 = Button(b_frame, text="Annyeong!", bg="white", fg="blue").pack(side="left")
'''side had 4 values= {left, right, top, bottom} '''
btnBtm2 = Button(b_frame, text="Jalga!", bg="white", fg="black").pack(side="right")

w.mainloop()
