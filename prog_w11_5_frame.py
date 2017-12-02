#using frame widget 
from tkinter import * 
root = Tk() 

frame = Frame(root)  
root.geometry("100x200") 

blackbutton = Button(frame, text="Black", fg="black") 
blackbutton.pack( side = TOP) 

redbutton = Button(frame, text="Red", fg="red") 
redbutton.pack( side = TOP) 

greenbutton = Button(frame, text="Brown", fg="brown") 
# padding 'padx' = create horizonal space of 10 pixces between 'Brown' and 'Blue'
greenbutton.pack( side = RIGHT, padx=10 )   

bluebutton = Button(frame, text="Blue", fg="blue") 
bluebutton.pack( side = LEFT ) 

frame.pack() 
frame.mainloop()