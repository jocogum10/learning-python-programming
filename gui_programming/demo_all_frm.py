"""
4 demo class components (subframes) on one window;
there are 5 Quitter buttons on this one windwo too, and each kills entire gui;
GUIs can be reused as frames in container, independent windows, or processes;
"""

from tkinter import *
from quitter import Quitter
demoModules = ['demo_dialog', 'demo_check', 'demo_radio', 'demo_scale']
parts = []

def addComponents(root):
    for demo in demoModules:
        module = __import__(demo)           #import by name string
        part = module.Demo(root)            # attach an instance
        part.config(bd=6, relief=RIDGE)
        part.pack(side=LEFT, expand=YES, fill=BOTH)
        parts.append(part)
        
def dumpState():
    for part in parts:
        print(part.__module__ + ':', end=' ')
        if hasattr(part, 'report'):
            part.report()
        else:
            print('none')
            
root = Tk()
root.title('Frame')
Label(root, text='Multiple Frame demo', bg='white').pack()
Button(root, text='States', command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
addComponents(root)
root.mainloop()