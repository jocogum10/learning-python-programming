import sys
from tkinter import Tk, Toplevel, Button, Label

root = Tk()
win1 = Toplevel()
win2 = Toplevel()

Button(win1, text='Spam', command=sys.exit).pack()
Button(win2, text='SPAM', command=sys.exit).pack()

Label(root, text='Popups').pack()
win1.mainloop()