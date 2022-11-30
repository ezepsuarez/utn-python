import os
from tkinter import *
import tkinter
from tkinter.ttk import Combobox, Notebook, Treeview, Style
from connection import crear_conexion, crear_tabla
from modelo import agregar, eliminar, listar, modificar

def interfaz(master):
    style = Style(master)
    master.title("Empresa Odino")
    master.geometry('1000x600')
    master.configure(background="#2F48D6")
    style.configure("Treeview", background="#e3e7fa", fieldbackground="#e3e7fa", foreground="black")
    master.option_add('*TCombobox*Listbox*Background', '#e3e7fa')
    master.option_add('*TCombobox*Listbox*Foreground', "#404040")
    master.option_add('*TCombobox*Listbox*selectBackground', "#404040")
    master.option_add('*TCombobox*Listbox*selectForeground', '#e3e7fa')
    style.map('TCombobox', fieldbackground=[('readonly', "#e3e7fa")])
    style.map('TCombobox', selectbackground=[('readonly', "#e3e7fa")])
    style.map('TCombobox', selectforeground=[('readonly', "#404040")])
    style.map('TCombobox', background=[('readonly', "#e3e7fa")])
    style.map('TCombobox', foreground=[('readonly', "#404040")])

    tree = Treeview(master)
    notebook = Notebook(master)
    notebook.grid(column=0, row=0, padx=25, pady=10)

    frame_agregar = Frame(notebook, width=950)
    frame_modificar = Frame(notebook, width=950)
    frame_eliminar = Frame(notebook, width=950)

    notebook.add(frame_agregar, text='Agregar')
    notebook.add(frame_modificar, text='Modificar')
    notebook.add(frame_eliminar, text='Eliminar')


    ### NOTEBOOK AGREGAR
    var_nombre_agregar = StringVar(master, "Juan")
    var_apellido_agregar = StringVar(master, "Perez")
    var_fecha_nacimiento_agregar = StringVar(master, "2022-12-31")
    var_puesto_agregar = StringVar(master, "Secretario")
    var_DNI_agregar = StringVar(master, "11111111")
    var_fecha_ingreso_agregar = StringVar(master, "2022-12-31")
    var_sexo_agregar = StringVar(master, "Masculino")
    var_sueldo_agregar = DoubleVar(master, 150000)
    var_nacionalidad_agregar = StringVar(master, "Argentina")

    label_nombre_agregar = Label(frame_agregar, text="Nombre: ")
    label_nombre_agregar.grid(pady=10, padx=10, row=1, column=0, sticky=E)
    entry_nombre_agregar = Entry(frame_agregar, textvariable=var_nombre_agregar, background="#e3e7fa")
    entry_nombre_agregar.grid(row=1, column=1)

    label_apellido_agregar = Label(frame_agregar, text="Apellido: ")
    label_apellido_agregar.grid(pady=10, padx=10, row=1, column=2, sticky=E)
    entry_apellido_agregar = Entry(frame_agregar, textvariable=var_apellido_agregar, background="#e3e7fa")
    entry_apellido_agregar.grid(row=1, column=3)

    label_nacionalidad_agregar = Label(frame_agregar, text="Nacionalidad: ")
    label_nacionalidad_agregar.grid(pady=10, padx=10, row=1, column=4, sticky=E)
    entry_nacionalidad_agregar = Entry(frame_agregar, textvariable=var_nacionalidad_agregar, background="#e3e7fa")
    entry_nacionalidad_agregar.grid(row=1, column=5)

    label_dni_agregar = Label(frame_agregar, text="DNI: ")
    label_dni_agregar.grid(pady=10, padx=10, row=2, column=0, sticky=E)
    entry_dni_agregar = Entry(frame_agregar, textvariable=var_DNI_agregar, background="#e3e7fa")
    entry_dni_agregar.grid(row=2, column=1)

    label_sexo_agregar = Label(frame_agregar, text="Sexo: ")
    label_sexo_agregar.grid(pady=10, padx=10, row=2, column=2, sticky=E)
    entry_sexo_agregar = Combobox(frame_agregar, textvariable=var_sexo_agregar, state="readonly", values=["Femenino", "Masculino"])
    entry_sexo_agregar.grid(row=2, column=3)

    label_fecha_nac_agregar = Label(frame_agregar, text="Fecha Nacimiento: ")
    label_fecha_nac_agregar.grid(pady=10, padx=10, row=2, column=4, sticky=E)
    entry_fecha_nac_agregar = Entry(frame_agregar, textvariable=var_fecha_nacimiento_agregar, background="#e3e7fa")
    entry_fecha_nac_agregar.grid(row=2, column=5)

    label_puesto_lab_agregar = Label(frame_agregar, text="Puesto Laboral: ")
    label_puesto_lab_agregar.grid(pady=10, padx=10, row=3, column=0, sticky=E)
    entry_puesto_lab_agregar = Entry(frame_agregar, textvariable=var_puesto_agregar, background="#e3e7fa")
    entry_puesto_lab_agregar.grid(row=3, column=1)

    label_sueldo_agregar = Label(frame_agregar, text="Sueldo: ")
    label_sueldo_agregar.grid(pady=10, padx=10, row=3, column=2, sticky=E)
    entry_sueldo_agregar = Entry(frame_agregar, textvariable=var_sueldo_agregar, background="#e3e7fa")
    entry_sueldo_agregar.grid(row=3, column=3)

    label_fecha_ing_agregar = Label(frame_agregar, text="Fecha Ingreso: ")
    label_fecha_ing_agregar.grid(pady=10, padx=10, row=3, column=4, sticky=E)
    entry_fecha_ing_agregar = Entry(frame_agregar, textvariable=var_fecha_ingreso_agregar, background="#e3e7fa")
    entry_fecha_ing_agregar.grid(row=3, column=5)

    boton_agregar = Button(frame_agregar, text="Agregar", command=lambda: agregar(
        var_nombre_agregar, 
        var_apellido_agregar, 
        var_DNI_agregar, 
        var_sexo_agregar, 
        var_sueldo_agregar, 
        var_nacionalidad_agregar, 
        var_fecha_nacimiento_agregar, 
        var_fecha_ingreso_agregar, 
        var_puesto_agregar, 
        tree, 
        con), background="#e3e7fa")
    boton_agregar.grid(row=4, column=3, pady=10, sticky=EW)


    ### NOTEBOOK MODIFICAR
    var_id_modificar = IntVar(master, 1)
    var_nombre_modificar = StringVar(master, "Pablo")
    var_apellido_modificar = StringVar(master, "Perez")
    var_puesto_modificar = StringVar(master, "Gerente")
    var_sueldo_modificar = DoubleVar(master, 200000)

    label_id_modificar = Label(frame_modificar, text="ID: ")
    label_id_modificar.grid(pady=10, padx=10, row=1, column=0, sticky=E)
    entry_id_modificar = Entry(frame_modificar, textvariable=var_id_modificar, background="#e3e7fa")
    entry_id_modificar.grid(row=1, column=1)

    label_nombre_modificar = Label(frame_modificar, text="Nombre: ")
    label_nombre_modificar.grid(pady=10, padx=10, row=1, column=2, sticky=E)
    entry_nombre_modificar = Entry(frame_modificar, textvariable=var_nombre_modificar, background="#e3e7fa")
    entry_nombre_modificar.grid(row=1, column=3)

    label_apellido_modificar = Label(frame_modificar, text="Apellido: ")
    label_apellido_modificar.grid(pady=10, padx=10, row=1, column=4, sticky=E)
    entry_apellido_modificar = Entry(frame_modificar, textvariable=var_apellido_modificar, background="#e3e7fa")
    entry_apellido_modificar.grid(row=1, column=5)

    label_sueldo_modificar = Label(frame_modificar, text="Sueldo: ")
    label_sueldo_modificar.grid(pady=10, padx=10, row=2, column=0, sticky=E)
    entry_sueldo_modificar = Entry(frame_modificar, textvariable=var_sueldo_modificar, background="#e3e7fa")
    entry_sueldo_modificar.grid(row=2, column=1)

    label_puesto_lab_modificar = Label(frame_modificar, text="Puesto Laboral: ")
    label_puesto_lab_modificar.grid(pady=10, padx=10, row=2, column=2, sticky=E)
    entry_puesto_lab_modificar = Entry(frame_modificar, textvariable=var_puesto_modificar, background="#e3e7fa")
    entry_puesto_lab_modificar.grid(row=2, column=3)

    boton_modificar = Button(frame_modificar, text="Modificar", command=lambda: modificar(
        var_id_modificar, 
        var_sueldo_modificar, 
        var_nombre_modificar, 
        var_apellido_modificar, 
        var_puesto_modificar, 
        tree, 
        con), background="#e3e7fa")
    boton_modificar.grid(row=4, column=3, pady=10, sticky=EW)


    ### NOTEBOOK ELIMINAR
    var_id_eliminar = IntVar(master, 1)

    label_id_eliminar = Label(frame_eliminar)
    label_id_eliminar.grid(pady=10, padx=135, row=1, column=0)
    label_id_eliminar = Label(frame_eliminar, text="ID: ")
    label_id_eliminar.grid(pady=10, padx=10, row=1, column=1, sticky=E)
    entry_id_eliminar = Entry(frame_eliminar, textvariable=var_id_eliminar, background="#e3e7fa")
    entry_id_eliminar.grid(row=1, column=2)

    boton_eliminar = Button(frame_eliminar, text="Eliminar", command=lambda: eliminar(var_id_eliminar, tree, con), background="#e3e7fa")
    boton_eliminar.grid(row=4, column=2, pady=10, sticky=EW)


    ### TREEVIEW
    tree.grid(padx=25, pady=15)
    tree["columns"] = ("id", "nombre", "apellido", "DNI", "sexo", "fecha_nacimiento", "nacionalidad", "puesto_laboral", "sueldo", "fecha_ingreso")

    tree.heading("id", text="ID")
    tree.heading("apellido", text="Apellido")
    tree.heading("nombre", text="Nombre")
    tree.heading("DNI", text="DNI")
    tree.heading("sexo", text="Sexo")
    tree.heading("nacionalidad", text="Nacionalidad")
    tree.heading("fecha_nacimiento", text="F. Nacimiento")
    tree.heading("puesto_laboral", text="Puesto")
    tree.heading("sueldo", text="Sueldo")
    tree.heading("fecha_ingreso", text="F. Ingreso")

    tree.column("#0", width=0)
    tree.column("id", width=50, minwidth=50, anchor=tkinter.CENTER)
    tree.column("apellido", width=100, minwidth=100, anchor=tkinter.CENTER)
    tree.column("nombre", width=100, minwidth=100, anchor=tkinter.CENTER)
    tree.column("DNI", width=80, minwidth=80, anchor=tkinter.CENTER)
    tree.column("sexo", width=50, minwidth=50, anchor=tkinter.CENTER)
    tree.column("nacionalidad", width=120, minwidth=120, anchor=tkinter.CENTER)
    tree.column("fecha_nacimiento", width=120, minwidth=120, anchor=tkinter.CENTER)
    tree.column("puesto_laboral", width=100, minwidth=100, anchor=tkinter.CENTER)
    tree.column("sueldo", width=100, minwidth=100, anchor=tkinter.CENTER)
    tree.column("fecha_ingreso", width=120, minwidth=100, anchor=tkinter.CENTER)

    if os.path.isfile("personas.db"):
        con = crear_conexion()
        listar(tree, con)
    else:
        con = crear_conexion()
        crear_tabla(con)
        listar(tree, con)