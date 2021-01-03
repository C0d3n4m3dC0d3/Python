#GUI Program - Login Form using tkinter

from tkinter import  *

window = Tk()
window.geometry("400x400")
window.title("Login Form")

#components
lbl1 = Label(window, text = "USERNAME").grid(row=0)
lbl2 = Label(window, text="PASSWORD").grid(row=1)

uname = Entry(window).grid(row=0, column=1)
pwd = Entry(window).grid(row=1, column=1)

btn = Button(window, text="Login", width="27").grid(row= 2, columnspan = 2)

window.mainloop()
