# using button widget. there are 15 widgets defined in Tkinter 
from tkinter import * 
from tkinter import messagebox  # have to be explicit imported because * won't include messagebox

root = Tk() 
root.geometry("300x400") 
def helloCallBack(): 
	msg=messagebox.showinfo( "Hello Python", "Hello World")
aButton = Button(root, text ="Hello Button", command = helloCallBack)
aButton.place(x=150,y=150)
root.mainloop()