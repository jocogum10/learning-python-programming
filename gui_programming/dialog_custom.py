import sys
from tkinter import *
makemodal = (len(sys.argv) > 1)

def dialog():
    win = Toplevel()
    Label(win, text='Hard drive reformatted!').pack()
    Button(win, text='OK', comman=win.destroy).pack()
    if makemodal:
        win.focus_set()
        win.grab_set()
        win.wait_window()
    print('dialog exit')
    
root = Tk()
Button(root, text='popup', command=dialog).pack()
root.mainloop()