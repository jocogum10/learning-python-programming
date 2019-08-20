"""
4 demo classes in independent top-level windows;
not processes: when on is quit all others go away, because all windows run in
the same processes here; make Tk() first here, else we get blank default window
"""

from tkinter import *
demoModules = ['demo_dialog', 'demo_check', 'demo_radio', 'demo_scale']

def makePopups(modnames):
    demoObjects = []
    for modname in modnames:
        module = __import__(modname)
        window = Toplevel()
        demo = module.Demo(window)
        window.title(module.__name__)
        demoObjects.append(demo)
    return demoObjects

def allstates(demoObjects):
    for obj in demoObjects:
        if hasattr(obj, 'report'):
            print(obj.__module__, end=' ')
            obj.report()
            
root = Tk()
root.title('Popups')
demos = makePopups(demoModules)
Label(root, text='Multiple Toplevel window demo', bg='white').pack()
Button(root, text='States', command=(lambda: allstates(demos))).pack(fill=X)
root.mainloop()