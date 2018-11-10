#! usr/bin/env python3.7


from tkinter import *
from random import random


def hide_show():
    if label.winfo_viewable():
        label.grid_remove()
    else:
        label.grid()
    

root = Tk()
label = Label(text='Я здесЬ!')
label.grid()
button = Button(command=hide_show, text="Спрятать/Показать")
button.grid()
root.mainloop()
