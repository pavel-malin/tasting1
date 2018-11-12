from tkinter import *

root = Tk()
def leftclick(event):
    print("left button")

def rightclick(event):
    print("right button")

button1 = Button(root, text='Нажми')
button1.pack()
button1.bind('<Button-1>', leftclick)
button1.bind('<Button-3>', rightclick)
root.mainloop()

