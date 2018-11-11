from tkinter import *

root = Tk()
listbox1 = Listbox(root, height=5, width=15, selectmode=EXTENDED)
listbox2 = Listbox(root, height=5, width=15, selectmode=SIGLE)
lis1 = ["Mockva", "Sankt-Petrburg", "Saratov", "Omck"]
list2 = ["Kamberra", "Signej", "Melbur", "Adelande"]
for i in list1:
    listbox1.insert(END,;)
for i in list2:
    listbox2.insert(END,;)

listbox1.pack()
listbox2.pack()
root.mainloop()
