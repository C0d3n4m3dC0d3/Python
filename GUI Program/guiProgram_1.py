#GUI Programming using Pyhton

#1. import tkinter module
import tkinter

#2. intialize the window manager
win = tkinter.Tk()
'''using the geometry() method, we can give the initial size for the window'''
win.geometry("500x200")

#3. (optional) rename the window
win.title("First pyGUI program!!")

#4. Define widgets
lbl = tkinter.Label(win, text="Hello, world!", height=4, width=10, bg="white", fg="green")

#5. Geomtry Management using pack()
'''Used for managing the width, height and position, etc'''
''' default position is center'''
lbl.pack()

#6. mainloop method
'''mainloop is used to close the window when the user clicks/presses a key'''
win.mainloop()
