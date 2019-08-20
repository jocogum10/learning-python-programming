"""
4 demo classes run as independent program processes: multiprocessing;
multiprocessing allows us to launch named functions with arguments,
but not lambdas, because they are not pickleable on windows (chapter5);
multiprocessing also has its own IPC tools like pipes for communication;
"""

from tkinter import *
from multiprocessing import Process
demoModules = ['demo_dialog', 'demo_radio', 'demo_check', 'demo_scale']

def runDemo(modname):
    module = __import__(modname)
    module.Demo().mainloop()
    
if __name__ == '__main__':
    for modname in demoModules:
        Process(target=runDemo, args=(modname,)).start()
        
    root = Tk()
    root.title('Processes')
    Label(root, text='Multiple program demo: multiprocessing', bg='white').pack()
    root.mainloop()