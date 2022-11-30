from doctest import master
from tkinter import Tk
from tkinter import StringVar
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import ttk
from tkinter.tix import Tree
import tkinter as GUI
from modelo import Abm
from modelo import BotonB
from modelo import Validacion

class VistaAplicacion():
    
    def __init__(self, window) -> None:
        self.master=window
        self.master.title("Aplicacion Entrega Final")
        self.obj=Abm()

        #Centramos la ventana
        self.width = 660 # Width 
        self.height = 510 # Height
        self.screen_width = self.master.winfo_screenwidth()  # Width of the screen
        self.screen_height = self.master.winfo_screenheight() # Height of the screen
        self.x = (self.screen_width/2) - (self.width/2)
        self.y = (self.screen_height/2) - (self.height/2)
        self.master.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))

        tabla=Validacion()
        tabla.existe_tabla()

        #Ponemos titulo
        self.titulo = Label(self.master, bd="10",fg="white" ,text="AMB de usuarios", width=100)
        self.titulo.grid(row=0, column=0, columnspan=6)
        self.titulo.config(bg="grey")

        self.var_mail= StringVar()
        self.var_nombre= StringVar()
        self.var_apellido = StringVar()
        self.var_preferencia= StringVar()
        self.var_sexo=StringVar()

        self.mail = Label(self.master, text="Email :")
        self.mail.grid(row=2, column=1, sticky="w")

        self.nombre = Label(self.master, text="Nombre :")
        self.nombre.grid(row=3, column=1, sticky="w")

        self.apellido = Label(self.master, text="Apellido :")
        self.apellido.grid(row=4, column=1, sticky="w")

        self.sexo = Label(self.master, text="Sexo :")
        self.sexo.grid(row=5, column=1, sticky="w")

        self.preferencia = Label(self.master, text="Preferencia :")
        self.preferencia.grid(row=6, column=1, sticky="w")

        self.mail = Entry(self.master, textvariable=self.var_mail, width=30)
        self.mail.grid (row=2, column=2,sticky="w")

        self.nombre = Entry(self.master, textvariable=self.var_nombre, width=30)
        self.nombre.grid (row=3, column=2,sticky="w")

        self.apellido = Entry(self.master, textvariable=self.var_apellido, width=30)
        self.apellido.grid (row=4, column=2,sticky="w")

        self.sexo = ttk.Combobox(self.master, state="readonly", textvariable=self.var_sexo, width=5)
        self.sexo['values']=('F', 'M')
        self.sexo.grid (row=5, column=2,sticky="w")

        categoria=Abm()
        lista_cat={}
        rows=categoria.carga_categoria()
        for row in rows:
            lista_cat[f"{row[0]} --> " f"{row[1]}"]= row[0]
            
        print(lista_cat)
        def my_upd(*args):
            self.var_preferencia.set(lista_cat[self.var_preferencia.get()]) # value of the key is displayed

        valores_categoria=list(lista_cat.keys())
        #self.preferencia = Entry(self.master, textvariable=self.var_preferencia, width=30)
        self.preferencia = ttk.Combobox(self.master, state="readonly",values=valores_categoria, textvariable=self.var_preferencia, width=30)
        self.var_preferencia.trace('w',my_upd)
        self.preferencia.grid (row=6, column=2,sticky="w")

        self.tree = ttk.Treeview(self.master,height=15)
        self.tree['columns'] = ("col1", "col2", "col3", "col4", "col5")
        self.tree.column("#0", width=50, minwidth=50, anchor="w")
        self.tree.heading("#0", text="ID")
        self.tree.column("col1", width=180, minwidth=180, anchor="w")
        self.tree.heading("col1", text="Email")
        self.tree.column("col2", width=80, minwidth=80, anchor="w")
        self.tree.heading("col2", text="Nombre")
        self.tree.column("col3", width=100, minwidth=100, anchor="w")
        self.tree.heading("col3", text="Apellido")
        self.tree.column("col4", width=70, minwidth=70, anchor="w")
        self.tree.heading("col4", text="Sexo")
        self.tree.column("col5", width=100, minwidth=100, anchor="w")
        self.tree.heading("col5", text="Preferencia")
        self.tree.grid(row=12, column=0, columnspan=5)

        boton_cancelar= BotonB(self.master, text=" Cancelar ", bg="#DC324C", command=lambda:None, state="disabled",  width=10, drow=5, dcol=4, dsti="w", ocultar="true")
        boton_guardar_cambio= BotonB(self.master, text=" Guardar ", bg="#4EDC32", command=lambda:None, state="disabled",  width=10, drow=5, dcol=3, dsti="w", ocultar="true")  
        boton_grabar =BotonB(self.master, text="Alta",  bg="#326DDC", command=lambda: self.obj.funcion_grabar(self.tree, self.var_mail, self.var_nombre, self.var_apellido, self.var_sexo, self.var_preferencia), width=10, drow=3, dcol=3, dsti="w")
        boton_eliminar =BotonB(self.master, text=" Baja ", bg="#DC3232", command=lambda: self.obj.funcion_eliminar(self.tree, self.var_mail, self.var_nombre, self.var_apellido, self.var_sexo, self.var_preferencia), width=10, drow=4, dcol=3, dsti="w")
        boton_consultar =BotonB(self.master, text=" Consulta ", bg="grey", command=lambda: self.obj.funcion_consultar(self.tree, self.var_mail, self.var_nombre, self.var_apellido, self.var_sexo, self.var_preferencia), width=10, drow=3, dcol=4, dsti="w")
        boton_modificacion =BotonB(self.master, text=" Modificar", bg="grey", command=lambda: self.obj.funcion_modificar(self.tree, self.master, self.var_mail, self.var_nombre, self.var_apellido, self.var_sexo, self.var_preferencia, boton_eliminar, boton_grabar,boton_consultar, boton_modificacion), width=10, drow=4, dcol=4, dsti="w")