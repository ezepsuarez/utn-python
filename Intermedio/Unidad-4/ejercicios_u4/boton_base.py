from tkinter import *
from parametros import bcolor, bfont, bsize

class BotonB:
    def __init__(self, parent=None, *args, **kwars):
        self.root=parent
        self.root.geometry("300x300")
        self.b1=Button(self.root, *args,**kwars)
        self.b1.pack(side=LEFT)
        self.b1.config(command=self.callback, bg=bcolor, font=(bfont, bsize))
        

    def callback(self,):
        print("Chau")
        #self.root.quit()
        self.b1.destroy()

if __name__=="__main__":
    root=Tk()
    mi_app = BotonB(root, text="Hola botón")
    root.mainloop()