from tkinter import *

root = Tk()
frame1 = Frame(root, bg='green', bd=5)
frame2 = Frame(root, bg='red', bd=5)
button1 = Button(frame1, text="1 button")
button2 = Button(frame2, text="2 button")

frame1.pack()
frame2.pack()
button1.pack()
button2.pack()
root.mainloop()
