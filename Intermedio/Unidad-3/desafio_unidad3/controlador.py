from tkinter import Tk
import vista


if __name__ == "__main__":

    # Se crea ventana de interfaz gráfica.
    master = Tk()

    # Se trae  contenido de la interfaz gráfica.
    vista.VistaAplicacion.vista_app(master)

    master.mainloop()