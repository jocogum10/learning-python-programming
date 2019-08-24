
from sys import argv
from tkinter import *
filename = argv[1] if len(argv) > 1 else "./images/1.png"

win = Tk()
img = PhotoImage(filename)
can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=img.width(), height=img.height())
can.create_image(2, 2, image=img, anchor=NW)
win.mainloop()