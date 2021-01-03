#unit 5
'''
Packages - matplotlib, numpy, pandas, etc
GUI Programming: Tkinter programming, Tkinter and Python Programming, TK Widgets, Tkinter Examples
'''
'''
Steps to do gui programming using tkinter
1. import the tkinter module (import tkinter)
2. initialize the window manager (tkinter.Tk())
    (window_obj.geometry("x*y") - initial size for the window)
3. (optional) rename the window (window_obj.title(title))
4. define widgets
    widget_name(window_object, text="display_text", height=h, width=w, bg="bgcolor", fg="fontcolor")
    widget_name(frame_object/window_object)
    Label | Button | Frame | CheckButtons | Entry 
5. geometry management using pack()
    widget_object.pack()
    widget_object.grid()
        - to specify position in a matrix like format i.e, rows and columns
6. mainloop method (window_object.mainloop())
'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Extras
    - to avoid using tkinter keyword use - from tkinter import *
    - pack() method can take a parameter 'side'  - it has 4 values {left, right, top, bottom}
    - grid() method takes 3 parameters - 'row' for the row index, 'column' for the column index, and
                                                               'sticky' for the stickyness character - n, e, w, s
                                                               to decide the side to whicht the widget should "stick"
    - to make a button responsive to click of the user, use command parameter of the constructor,
        and pass the function name which to call when the button is pressed
'''


#Simple Registration Form using Tkinter

from tkinter import *

window = Tk()
window.geometry("250x250")
window.title("Course Registration")

#labels
lbl_title = Label(window, text="Course Registration", fg="brown").grid(row = 0, column= 1, columnspan = 5)
lbl_name = Label(window, text = "Name:", fg ="indigo").grid(row = 1, columnspan = 2, sticky="E")
lbl_age = Label(window, text = "Age:", fg ="indigo").grid(row=2, columnspan = 2, sticky="E")
lbl_course = Label(window, text = "Course:", fg ="indigo").grid(row=3, columnspan = 2, sticky="E")
lbl_year = Label(window, text ="Year:", fg ="indigo").grid(row=4, columnspan = 2,sticky="E")
lbl_subject = Label(window, text = "Subjects:", fg ="indigo").grid(row=5, columnspan = 2, sticky="E")


#textboxes
name = Entry(window, fg ="green").grid(row = 1, column = 3,   columnspan = 2, sticky = "W")
age = Entry(window, fg="green").grid(row = 2, column = 3,   columnspan = 2, sticky = "W")
course = Entry(window, fg = "green").grid(row = 3, column = 3,   columnspan = 2, sticky = "W")
year = Entry(window, fg = "green").grid(row = 4, column = 3,   columnspan = 2, sticky = "W")


#check buttons
java = Checkbutton(window, text="Java", fg="red").grid(row=5, column= 3, sticky="W")
cSharp = Checkbutton(window, text="C#", fg="purple").grid(row=5, column= 4, sticky="W")
python = Checkbutton(window, text="Python", fg="blue").grid(row=6, column= 3, sticky="W")
c = Checkbutton(window, text="C").grid(row=6, column= 4, sticky="W")

#button
def collect():
    Label(window, text="Registered!", bg="white", fg="green").grid(row=8, columnspan=5)


btn = Button(window, text="Register", command=collect).grid(row =7 , columnspan=5)

window.mainloop()
