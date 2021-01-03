#GUI Program - For button functionality

from tkinter import *

win = Tk()
win.geometry("250x250")
win.title("Command Example")

#create a function
def testTK():
    l = Label(win, text="Check command prompt").pack()
    for i in range(5):
        for j in range(i):
            print("*", end="")
        print()

btn = Button(win, text="Click me!", command=testTK).pack()

win.mainloop()
