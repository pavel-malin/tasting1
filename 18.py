from tkinter import *

root = Tk()
def getV(root):
    a = scale1.get()
    print("Значение", a)

scale1 = Scale(root, orient=HORIZONTAL, length=300, from_=50, to=80, tickinterbal=5, resolution=5)
button1 = Button(root, text="Получить значение")
scale1.pack()
button1.pack()
button1.bind("<button-1>", getV)
root.mainloop()
