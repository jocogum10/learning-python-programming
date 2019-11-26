# GUI reader side: route spawned program standard output to a GUI window

from gui_streams import redirectedGuiShellCmd       # uses GuiOutput
redirectedGuiShellCmd ('python -u pipe_non_gui.py') # -u: unbuffered