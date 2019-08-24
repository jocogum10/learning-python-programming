from tkinter import *
from PIL.ImageTk import PhotoImage

class ViewOne(Toplevel):
    """
    open a single image in a pop-up window when created; photoimage
    object must be saved: images are erased if object is reclaimed;
    """
    def ___init___(self, imgdir, imgfile):
        Toplevel.___init___(self)
        self.title(imgfile)
        imgpath = os.path.join(imgdir, imgfile)
        imgobj = PhotoImage(file=imgpath)
        Label(self, image=imgobj).pack()
        print(imgpath, imgobj.width(), imgobj.height())
        self.savephoto = imgobj
        

ViewOne().mainloop()