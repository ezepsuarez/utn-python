from tkinter import *
from parametros import bcolor, bfont, bsize

class BotonB:
    def __init__(self, val1, **kwars):
        self.val1=val1
        self.nombre=kwars.get('nombre')
        self.apellido=kwars.get('apellido')
        self.edad=kwars.get('edad')
        print(self.val1)
        print(self.nombre)
        print(self.apellido)
        print(self.edad)
  

if __name__=="__main__":
    root=Tk()
    mi_app = BotonB(val1="ddd", nombre="oscar", apellido="perez", edad=10 )
    root.mainloop()