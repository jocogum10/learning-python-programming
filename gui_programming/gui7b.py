from tkinter import *
from gui7 import HelloPackage

frm = Frame()
frm.pack()
Label(frm, text='Hello').pack()

part = HelloPackage(frm)
part.pack(side=RIGHT)           # fail -- need part.top.pack(side=RIGHT); use 'from gui7c import HelloPackage' instead
frm.mainloop()