'''
Tkinter widgets can be organized within the parent widget (window) by geometry management classes or managers; they are implemented as 3 methods:
1) Pack(): it organizes the widgets in blocks into the parent window.
2) Grid(): it places widgets in a 2D tabl (rows and columns). The position of a widget is defined by the row and column numbers.
3) Place(): it places widgets in a specific pre-defined positions (x= ,y= )in the parent widget.
'''
#using pack manager 
from tkinter import * 

root = Tk() 
Label(root, text="Red Sun", bg="red", fg="white").pack() 
Label(root, text="Green Grass", bg="green", fg="black").pack() 
Label(root, text="Blue Sky", bg="blue", fg="white").pack() 
mainloop()


# using grid manager 
#from tkinter import * 
colours = ['red','green','orange','white','yellow','blue'] 
r = 0
for c in colours: 
	Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0) 
	Entry(bg=c, relief=SUNKEN,width=10).grid(row=r,column=1) 
	r = r + 1 
mainloop()