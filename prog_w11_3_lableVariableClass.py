# using label widget
# Variable classes

from tkinter import * 

root = Tk() 

'''
Some widgets can be associated directly to Tkinter application variables by using special parameters (e.g. onvalue, offvalue and value). These variables are very important because we can not pass Python variables to Tkinter widgets. Only variables classes can be used in this case.
'''
# Variable classes
var = StringVar()

label=Label(root, textvariable=var, relief=SUNKEN) # FLAT
#label=Label(root, textvariable=var, relief=FLAT)   
var.set("Good morning? How are you?")
print(var.get())
label.pack()
root.mainloop()