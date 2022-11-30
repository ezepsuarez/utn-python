from tkinter import Tk
import vista


if __name__ == "__main__":

    # Se crea ventana de interfaz gráfica.
    root = Tk()

    # Se trae  contenido de la interfaz gráfica.
    vista.vista_app(root)

    root.mainloop()
