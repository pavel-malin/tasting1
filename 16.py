from tkinter import *

root =Tk()
var1 = IntVar()
var2 = IntVar()
check1 = Checkbutton(root, text='1 start', variable=var1, onvalue=1, offvalue=0)
check2 = Checkbutton(root, text='2 start', variable=var2, onvalue=1, offvalue=0)
check1.pack()
check2.pack()
root.mainloop()
