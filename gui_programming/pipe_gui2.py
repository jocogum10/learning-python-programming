# GUI reader side: like pipes_gui1, but make root window and mainloop explicit

from tkinter import *
from gui_streams import redirectedGuiShellCmd

def launch():
    import _thread
    _thread.start_new_thread(redirectedGuiShellCmd, ('python -u pipe_non_gui.py',))
    
window = Tk()
Button(window, text='GO!', command=launch).pack()
window.mainloop()