from modelo import BasesDatos
from tkinter import StringVar
from tkinter import Label
from tkinter import Entry
from tkinter import ttk
from tkinter import Button


class MiVista:
    def __init__(self, window):
        self.planilla = window
        self.planilla.title("TAREA CLASE 3")
        self.demodelo = BasesDatos()
        self.nom = StringVar()
        self.apel = StringVar()
        self.mate = StringVar()
        self.notaa = StringVar()
        self.titulo = Label(
            self.planilla,
            text="SISTEMA DE CONTROL DE ALUMNADO",
            bg="#6C34FA",
            fg="white",
            height=1,
            width=100,
        )
        self.titulo.grid(
            row=0, column=0, columnspan=5, padx=1, pady=1, sticky="w" + "e"
        )
        self.nombre = Label(self.planilla, text="NOMBRE")
        self.nombre.grid(row=1, column=0, sticky="w")
        self.apellido = Label(self.planilla, text="APELLIDO")
        self.apellido.grid(row=2, column=0, sticky="w")
        self.materia = Label(self.planilla, text="MATERIA")
        self.materia.grid(row=3, column=0, sticky="w")
        self.nota = Label(self.planilla, text="NOTA")
        self.nota.grid(row=4, column=0, sticky="w")

        ################# CAMPOS DE ENTRADA DE DATOS #############

        self.entry_nombre = Entry(self.planilla, textvariable=self.nom, width=30)
        self.entry_nombre.grid(row=1, column=2)
        self.entry_apellido = Entry(self.planilla, textvariable=self.apel, width=30)
        self.entry_apellido.grid(row=2, column=2)
        self.entry_materia = Entry(self.planilla, textvariable=self.mate, width=30)
        self.entry_materia.grid(row=3, column=2)
        self.entry_nota = Entry(self.planilla, textvariable=self.notaa, width=30)
        self.entry_nota.grid(row=4, column=2)

        ###################### T R E E V I E W ###############################

        self.tree = ttk.Treeview(self.planilla)

        self.tree["columns"] = (
            "col1",
            "col2",
            "col3",
            "col4",
        )
        self.tree.column("#0", width=30, minwidth=50, anchor="w")
        self.tree.column("col1", width=200, minwidth=80, anchor="w")
        self.tree.column("col2", width=200, minwidth=80, anchor="w")
        self.tree.column("col3", width=200, minwidth=80, anchor="w")
        self.tree.column("col4", width=30, minwidth=80, anchor="w")
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Nombre")
        self.tree.heading("col2", text="Apellido")
        self.tree.heading("col3", text="Materia")
        self.tree.heading("col4", text="Nota")

        self.tree.grid(column=0, row=7, columnspan=4)

        ###################### B O T O N E S ###############################

        self.boton_alta = Button(
            self.planilla, text="Alta", command=lambda: self.alta()
        )
        self.boton_alta.grid(row=1, column=3)

        self.boton_borrar = Button(
            self.planilla, text="Baja", command=lambda: self.borrar()
        )
        self.boton_borrar.grid(row=2, column=3)

        self.boton_consulta = Button(
            self.planilla,
            text="Consulta",
            command=lambda: self.demodelo.consultar(self.tree),
        )
        self.boton_consulta.grid(row=3, column=3)

        self.boton_salir = Button(
            self.planilla, text="Salir", command=self.planilla.quit
        )

        self.boton_salir.grid(row=4, column=3)

        self.boton_modifica_no = Button(
            self.planilla,
            text="Modificar NOMBRE",
            command=lambda: self.modifica_no(),
        )
        self.boton_modifica_no.grid(row=1, column=4)

        self.boton_modifica_ap = Button(
            self.planilla,
            text="Modificar APELLIDO",
            command=lambda: self.modifica_ap(),
        )
        self.boton_modifica_ap.grid(row=2, column=4)

        self.boton_modifica_ma = Button(
            self.planilla,
            text="Modificar MATERIA",
            command=lambda: self.modifica_materia(),
        )
        self.boton_modifica_ma.grid(row=3, column=4)

        self.boton_modifica_nt = Button(
            self.planilla,
            text="Modificar NOTA",
            command=lambda: self.modifica_nota(),
        )
        self.boton_modifica_nt.grid(row=4, column=4)

        self.boton_modifica_no.grid(row=1, column=4)

    def alta(
        self,
    ):
        self.demodelo.alta(self.nom, self.apel, self.mate, self.notaa, self.tree)

    def actualiza(
        self,
    ):
        self.demodelo.actualizar_treeview(self.tree)

    def borrar(
        self,
    ):
        self.demodelo.borrar(self.tree)

    def modifica_no(
        self,
    ):
        self.demodelo.modificar_no(self.nom, self.tree)

    def modifica_ap(
        self,
    ):
        self.demodelo.modificar_ap(self.apel, self.tree)

    def modifica_materia(
        self,
    ):
        self.demodelo.modificar_ma(self.mate, self.tree)

    def modifica_nota(
        self,
    ):
        self.demodelo.modificar_nt(self.notaa, self.tree)
