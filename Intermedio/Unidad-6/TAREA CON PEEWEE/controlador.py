from tkinter import Tk
from peewee import *
import vista


class Controladora:
    def __init__(self, planilla):
        self.planilla_controladora = planilla
        self.objeto_vista = vista.MiVista(self.planilla_controladora)


if __name__ == "__main__":
    planilla_tk = Tk()

    aplicacion = Controladora(planilla_tk)
    aplicacion.objeto_vista.actualiza()

    planilla_tk.mainloop()
