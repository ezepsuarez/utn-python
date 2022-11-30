from tkinter import Tk
from tkinter import Menu
from tkinter import StringVar
from tkinter import IntVar
from tkinter import LabelFrame
from tkinter import Label
from tkinter import Entry
from tkinter import CENTER
from tkinter import Button
from tkinter import ttk

import modelo


def vista_app(root):

    # Se conecta la infterfaz gráfica a la base de datos.
    conectar = modelo.base()
    modelo.tabla(conectar)

    # Se establece barra de menú de la inferfaz gráfica.
    menu_barra = Menu(root)
    menu_archivo = Menu(menu_barra, tearoff=0)
    menu_archivo.add_command(label="Salir", command=lambda: modelo.salir(root))
    menu_barra.add_cascade(label="Archivo", menu=menu_archivo)
    root.config(menu=menu_barra)

    # Se definen las variables de los campos de entrada.
    var_genero = StringVar()
    var_apellido = StringVar()
    var_nombres = StringVar()
    var_titulo = StringVar()
    var_cantidad = IntVar()

    variables = [var_genero, var_apellido, var_nombres, var_titulo, var_cantidad]

    # Se configura el título y la dimensión de la interfaz gráfica.
    root.title("App Biblioteca - Menú Libros")
    root.geometry("654x408")

    # Se define un marco para etiquetas, campos de entrada y botones.
    frame = LabelFrame(
        root,
        text="Ingreso de Datos: ",
        fg="blue",
        height=165,
        width=631,
    )
    frame.place(x=5, y=5)

    # Se definenen las etiquetas de los campos de entrada.
    etiqueta_1 = Label(frame, text="Género Literario:")
    etiqueta_1.place(x=10, y=5)
    etiqueta_2 = Label(frame, text="Apellido:")
    etiqueta_2.place(x=10, y=32)
    etiqueta_3 = Label(frame, text="Nombres:")
    etiqueta_3.place(x=10, y=59)
    etiqueta_4 = Label(frame, text="Título:")
    etiqueta_4.place(x=10, y=86)
    etiqueta_5 = Label(frame, text="Cantidad de Ejemplares:")
    etiqueta_5.place(x=10, y=113)

    # Se define combobox y campos de entrada.
    combobox_genero = ttk.Combobox(
        frame,
        textvariable=var_genero,
        values=[
            "Ciencias",
            "Clásicos",
            "Historia",
            "Literatura argentina",
            "Literatura universal",
            "Literatura latinoamericana",
        ],
        width=30,
    )
    combobox_genero.place(x=180, y=5)

    entrada_apellido = Entry(frame, textvariable=var_apellido, width=30)
    entrada_apellido.place(x=180, y=32)
    entrada_nombres = Entry(frame, textvariable=var_nombres, width=30)
    entrada_nombres.place(x=180, y=59)
    entrada_titulo = Entry(frame, textvariable=var_titulo, width=30)
    entrada_titulo.place(x=180, y=86)
    entrada_cantidad = Entry(frame, textvariable=var_cantidad, width=30)
    entrada_cantidad.place(x=180, y=113)

    entradas = [
        combobox_genero,
        entrada_apellido,
        entrada_nombres,
        entrada_titulo,
        entrada_cantidad,
    ]

    # Se establece visor de registros.
    tree = ttk.Treeview(root)
    style = ttk.Style()
    style.theme_use("default")
    tree.place(x=5, y=179)

    # Se establece barra de desplazamiento para el visor de registros.
    tree_scroll = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree_scroll.place(x=636, y=179, height=221)
    tree.configure(yscrollcommand=tree_scroll.set)

    # Se definen las columnas y los encabezados del visor de registros.
    tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
    tree.column("#0", width=45)
    tree.column("col1", width=125)
    tree.column("col2", width=125)
    tree.column("col3", width=125)
    tree.column("col4", width=140)
    tree.column("col5", width=70, anchor=CENTER)

    tree.heading("#0", text="ID", anchor=CENTER)
    tree.heading("col1", text="Género Literario", anchor=CENTER)
    tree.heading("col2", text="Apellido", anchor=CENTER)
    tree.heading("col3", text="Nombres", anchor=CENTER)
    tree.heading("col4", text="Título", anchor=CENTER)
    tree.heading("col5", text="Cantidad", anchor=CENTER)

    # Se define evento para seleccionar registros con doble click.
    tree.bind(
        "<Double-1>",
        lambda evento, tree=tree, entradas=entradas, variables=variables: modelo.seleccion(
            tree, entradas, variables
        ),
    )

    # Se definen los botones para la ejecución de los comandos.
    boton_alta = Button(
        frame,
        text="Alta",
        width=15,
        command=lambda: modelo.alta(
            conectar,
            tree,
            variables,
        ),
    )
    boton_alta.place(x=498, y=5)

    boton_baja = Button(
        frame,
        text="Baja",
        width=15,
        command=lambda: modelo.baja(conectar, tree, variables),
    )
    boton_baja.place(x=498, y=32)

    boton_modificar = Button(
        frame,
        text="Modificar",
        width=15,
        command=lambda: modelo.modificar(
            conectar,
            tree,
            variables,
        ),
    )
    boton_modificar.place(x=498, y=59)

    boton_consultar = Button(
        frame,
        text="Consultar",
        width=15,
        command=lambda: modelo.consultar(conectar, tree, var_apellido.get()),
    )
    boton_consultar.place(x=498, y=86)

    boton_limpiar = Button(
        frame,
        text="Limpiar",
        width=15,
        command=lambda: modelo.limpiar(variables),
    )
    boton_limpiar.place(x=498, y=113)

    # Se limplian los campos de entrada.
    modelo.limpiar(variables)
