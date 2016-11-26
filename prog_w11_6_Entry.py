#using Entry widget
from tkinter import *
top = Tk()

L1=Label(top, text="User name")
L1.pack( side = RIGHT)

E1 = Entry(top, bd=5, bg="yellow", fg="purple")
E1.pack(side = RIGHT)
top.mainloop()