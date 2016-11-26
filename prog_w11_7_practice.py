from tkinter import *

root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)


L1=Label(frame1, text="label box # 1")
L1.pack( side = LEFT)
E1 = Entry(frame1, bd=5, bg="yellow", fg="purple")
E1.pack(side = RIGHT)

L2=Label(frame2, text="label box # 2")
L2.pack( side = LEFT)
E2 = Entry(frame2, bd=5, bg="blue", fg="red")
E2.pack(side = RIGHT)

aButton1 = Button(frame3, text ="Button#1")
aButton2 = Button(frame3, text ="Button#2")
aButton3 = Button(frame3, text ="Button#3")
aButton4 = Button(frame3, text ="Button#4")

scrollbar = Scrollbar(frame4) 


frame1.pack()
frame2.pack() 
aButton1.pack(side = LEFT, padx=3 ) 
aButton2.pack(side = LEFT, padx=3 ) 
aButton3.pack(side = LEFT, padx=3 )
aButton4.pack(side = LEFT, padx=3 )  
frame3.pack()
scrollbar.pack( side = BOTTOM, fill=Y)

frame4.pack() 
root.mainloop()