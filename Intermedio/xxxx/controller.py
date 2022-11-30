from tkinter import Tk
import vista


class Controller:
    """
    Clase Principal - Controlador
    """

    def __init__(self, root):
        self.tk_root_controler = root
        self.objeto_vista = vista.Vista_tk(self.tk_root_controler)


if __name__ == "__main__":
    tk_root = Tk()
    Controller(tk_root)
    tk_root.mainloop()
