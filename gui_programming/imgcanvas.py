imgdir = "./images/"
from tkinter import *
win = Tk()
img = PhotoImage(file=imgdir + "2.png")
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(2, 2, image=img, anchor=NW)
win.mainloop()