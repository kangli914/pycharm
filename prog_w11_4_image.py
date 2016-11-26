from tkinter import * 

root = Tk()
logo = PhotoImage(file="google.jpg")
explanation = '''This is a dummy image.'''
w = Label(root, 
		compound = CENTER, 
		text=explanation, 
		fg="RED", 
		image=logo).pack(side="left")

root.mainloop()