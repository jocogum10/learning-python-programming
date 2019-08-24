"""
show one image with standard tkinter photo object;
as is this handles GIF files, but not JPEG images; image filename listed in
command line, or default; use a canvas instead of label for scrolling, etc.
"""

import os, sys
from tkinter import *

imgdir = 'images'
imgfile = '1.png'
if len(sys.argv) > 1:
    imgfile = sys.argv[1]
imgpath = os.path.join(imgdir, imgfile)

win = Tk()
win.title(imgfile)
imgobj = PhotoImage(file=imgpath)
Label(win, image=imgobj).pack()
print(imgobj.width(), imgobj.height())
win.mainloop()