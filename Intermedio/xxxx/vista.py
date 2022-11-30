from tkinter import Button, Entry, IntVar, Label, StringVar, Tk, ttk
from tkinter.messagebox import *
from modelo import Crud
from tkinter.messagebox import *

class Vista_tk:
    def __init__(self, win):
        self.tk_root = win
        self.tk_root.title("Clientes")
        self.obje = Crud()

        self.titulo = Label(
            self.tk_root,
            text="Sistema de Administracion de Clientes",
            bg="Green",
            fg="thistle1",
            height=1,
            width=60,
        )
        self.titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="we")

        self.Nombre = Label(self.tk_root, text="Nombre")
        self.Nombre.grid(row=1, column=0, sticky="w")
        self.Apellido = Label(self.tk_root, text="Apellido")
        self.Apellido.grid(row=2, column=0, sticky="w")
        self.Edad = Label(self.tk_root, text="Edad")
        self.Edad.grid(row=3, column=0, sticky="w")
        self.dni = Label(self.tk_root, text="DNI")
        self.dni.grid(row=4, column=0, sticky="w")
        self.brdni = Label(self.tk_root, text="Ingrese DNI")
        self.brdni.grid(row=3, column=2, sticky="we")

        self.nom_val, self.ape_val = StringVar(), StringVar()
        w_ancho = 20
        self.ed_val, self.dni_val, self.brdni = IntVar(), IntVar(), IntVar()
        w_ancho = 20

        self.nombre = Entry(self.tk_root, textvariable=self.nom_val, width=w_ancho)
        self.nombre.grid(row=1, column=1)
        self.apellido = Entry(self.tk_root, textvariable=self.ape_val, width=w_ancho)
        self.apellido.grid(row=2, column=1)
        self.edad = Entry(self.tk_root, textvariable=self.ed_val, width=w_ancho)
        self.edad.grid(row=3, column=1)
        self.dni = Entry(self.tk_root, textvariable=self.dni_val, width=w_ancho)
        self.dni.grid(row=4, column=1)
        self.brdni = Entry(self.tk_root, textvariable=self.brdni, width=w_ancho)
        self.brdni.grid(row=2, column=2)

        self.tree = ttk.Treeview(self.tk_root)
        self.tree["columns"] = ("col1", "col2", "col3", "col4")
        self.tree.column("#0", width=90, minwidth=50, anchor="w")
        self.tree.column("col1", width=200, minwidth=80)
        self.tree.column("col2", width=200, minwidth=80)
        self.tree.column("col3", width=200, minwidth=80)
        self.tree.column("col4", width=200, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Nombre")
        self.tree.heading("col2", text="Apellido")
        self.tree.heading("col3", text="Edad")
        self.tree.heading("col4", text="DNI")
        self.tree.grid(row=10, column=0, columnspan=4)

        self.boton_alta = Button(
            self.tk_root,
            text="Alta",
            command=lambda: self.admin_alta(),
        )
        self.boton_alta.grid(row=6, column=1)

        self.boton_consulta = Button(
            self.tk_root,
            text="Consultar un registro",
            command=lambda: self.obje.buscar_registro(self.brdni.get(), self.tree),
        )
        self.boton_consulta.grid(row=2, column=3)

        self.boton_borrar = Button(
            self.tk_root, text="Borrar", command=lambda: self.obje.eliminar(self.tree)
        )
        self.boton_borrar.grid(row=7, column=1)

        self.boton_modificar = Button(
            self.tk_root,
            text="Modificar",
            command=lambda: self.obje.modificar_registro(
                self.nom_val.get(),
                self.ape_val.get(),
                self.ed_val.get(),
                self.dni_val.get(),
                self.tree,
            ),
        )
        self.boton_modificar.grid(row=6, column=2)

        self.boton_actualizar_tw = Button(
            self.tk_root,
            text="Actualizar",
            command=lambda: self.obje.actualizar_treeview(self.tree),
        )
        self.boton_actualizar_tw.grid(row=7, column=2)

    def admin_alta(self,):
        retorno=self.obje.alta(
                self.nom_val,
                self.ape_val,
                self.ed_val,
                self.dni_val,
                self.tree,
            )
        messagebox.showwarning(
            message="retorno", title="Información"
        )    

if __name__ == "__main__":
    tk_root = Tk()
    Vista_tk(tk_root)
    tk_root.mainloop()
