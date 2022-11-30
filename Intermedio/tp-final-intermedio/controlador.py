from tkinter import Tk
import vista

class Controller:

    def __init__(self, master):
        self.master_controler=master
        self.objeto_vista=vista.VistaAplicacion(self.master_controler)

if __name__=="__main__":
    master=Tk()
    Controller(master)
    master.mainloop()