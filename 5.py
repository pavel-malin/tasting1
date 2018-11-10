from tkinter import *


root = Tk()
root.after(200, root.grab_set_global)
root.after(1000, root.grab_release)
root.mainloop()
