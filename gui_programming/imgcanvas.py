from tkinter import *
win = Tk()
img = PhotoImage("..\ble_picture.png")
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(2, 2, image=img, anchor=NW)
win.mainloop()