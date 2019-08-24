imgdir = "./images/"
from tkinter import *
win = Tk()
igm = PhotoImage(file=imgdir + "1.png")
Button(win, image=igm).pack(side=TOP, expand=YES, fill=BOTH)
win.mainloop()