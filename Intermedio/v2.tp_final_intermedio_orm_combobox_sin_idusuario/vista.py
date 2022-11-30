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
from modelo import Validacion
from modelo import Pantalla
from tkinter import DISABLED, NORMAL, font
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
from tkinter.messagebox import showwarning


class VistaAplicacion():
    def __init__(self, window) -> None:
        self.master = window
        self.master.title("Aplicacion Entrega Final - Intermedio")
        self.obj = Abm()

        self.width = 660
        self.height = 510
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()
        self.x = (self.screen_width/2) - (self.width/2)
        self.y = (self.screen_height/2) - (self.height/2)
        self.master.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))

        self.titulo = Label(self.master, bd="10", fg="white", text="AMB de usuarios", width=100)
        self.titulo.grid(row=0, column=0, columnspan=6)
        self.titulo.config(bg="grey")

        self.var_mail = StringVar()
        self.var_nombre = StringVar()
        self.var_apellido = StringVar()
        self.var_preferencia = StringVar()
        self.var_sexo = StringVar()

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
        self.mail.grid(row=2, column=2, sticky="w")

        self.nombre = Entry(self.master, textvariable=self.var_nombre, width=30)
        self.nombre.grid(row=3, column=2, sticky="w")

        self.apellido = Entry(self.master, textvariable=self.var_apellido, width=30)
        self.apellido.grid(row=4, column=2, sticky="w")

        self.sexo = ttk.Combobox(self.master, state="readonly", textvariable=self.var_sexo, width=5)
        self.sexo['values']=('F', 'M')
        self.sexo.grid(row=5, column=2, sticky="w")
        lista_cat = {}
        datoscat = self.obj.carga_categoria()
        for row in datoscat:
            lista_cat[f"{row.id} --> " f"{row.descripcion_categoria}"] = row.id

        def mycat(*args):
            z=self.var_preferencia.get()
            for key, i in lista_cat.items():
                if (key == z):
                    self.var_preferencia.set(i)
                    
        valores_categoria = list(lista_cat.keys())
        self.preferencia = ttk.Combobox(self.master, state="readonly", values=valores_categoria, textvariable=self.var_preferencia, width=30)
        self.var_preferencia.trace('w', mycat)
        self.preferencia.grid(row=6, column=2, sticky="w")

        self.tree = ttk.Treeview(self.master, height=15)
        self.tree['columns'] = ("col1", "col2", "col3", "col4")
        self.tree.column("#0", width=180, minwidth=180, anchor="w")
        self.tree.heading("#0", text="Email")
        self.tree.column("col1", width=100, minwidth=80, anchor="w")
        self.tree.heading("col1", text="Nombre")
        self.tree.column("col2", width=100, minwidth=100, anchor="w")
        self.tree.heading("col2", text="Apellido")
        self.tree.column("col3", width=70, minwidth=70, anchor="w")
        self.tree.heading("col3", text="Sexo")
        self.tree.column("col4", width=100, minwidth=100, anchor="w")
        self.tree.heading("col4", text="Preferencia")
        self.tree.grid(row=12, column=0, columnspan=5,padx=5,pady=15)
        #boton_grabar = Button(master, text=" Alta ", bg="#326DDC", command=lambda: self.obj.funcion_grabar(self.tree, self.var_mail, self.var_nombre, self.var_apellido, self.var_sexo, self.var_preferencia), width=10)
        self.boton_grabar = Button(master, text=" Alta ", bg="#326DDC", command=lambda: self.admin_guardar(), width=10)
        self.boton_grabar.grid(row=3, column=3, sticky='W')
        #boton_eliminar = Button(master, text=" Baja ", bg="#DC3232", command=lambda: self.obj.funcion_eliminar(self.tree, self.var_mail, self.var_nombre, self.var_apellido, self.var_sexo, self.var_preferencia), width=10)
        self.boton_eliminar = Button(master, text=" Baja ", bg="#DC3232", command=lambda: self.admin_eliminar(), width=10)
        self.boton_eliminar.grid(row=4, column=3, sticky='W')
        self.boton_consultar = Button(master, text=" Consulta ", bg="grey", command=lambda: self.admin_consultar(), width=10)
        #boton_consultar = Button(master, text=" Consulta ", bg="grey", command=lambda: self.obj.funcion_consultar(self.tree, self.var_mail, self.var_nombre, self.var_apellido, self.var_sexo, self.var_preferencia), width=10)
        self.boton_consultar.grid(row=3, column=4, sticky='W')
        #boton_modificacion = Button(master, text=" Modificar", bg="grey", command=lambda: self.obj.funcion_modificar(self.tree, self.master, self.var_mail, self.var_nombre, self.var_apellido, self.var_sexo, self.var_preferencia, boton_eliminar, boton_grabar, boton_consultar, boton_modificacion), width=10)
        self.boton_modificacion = Button(master, text=" Modificar", bg="grey", command=lambda: self.admin_modificar(), width=10)
        self.boton_modificacion.grid(row=4, column=4, sticky='W')

    def admin_guardar(self,):
        respuesta = self.obj.funcion_grabar(
                    self.tree,
                    self.var_mail,
                    self.var_nombre,
                    self.var_apellido,
                    self.var_sexo,
                    self.var_preferencia
        )
        if respuesta[0] == '1':
            showinfo("Alta usuario", f"{respuesta[1]}")
        else:
            showwarning("Alta usuario", f"{respuesta[1]}")

    def admin_eliminar(self,):
        respuesta = self.obj.funcion_eliminar(
                    self.tree,
                    self.var_mail,
                    self.var_nombre,
                    self.var_apellido,
                    self.var_sexo,
                    self.var_preferencia
        )
        if respuesta[0] == '1':
            showinfo("Eliminacion usuario", f"{respuesta[1]}")
        else:
            showwarning("Eliminacion usuario", f"{respuesta[1]}")
    
    def admin_consultar(self,):
        respuesta = self.obj.funcion_consultar(
                    self.tree,
                    self.var_mail,
                    self.var_nombre,
                    self.var_apellido,
                    self.var_sexo,
                    self.var_preferencia
        )
        if respuesta[0] == '0':
            showinfo("Busqueda", f"{respuesta[1]}")

    def admin_modificar(self,):
        respuesta = self.obj.funcion_modificar(
                    self.tree, 
                    self.master, 
                    self.var_mail, 
                    self.var_nombre, 
                    self.var_apellido, 
                    self.var_sexo, 
                    self.var_preferencia
        )
        if respuesta[0] == '2':
            showwarning("Modificacion", f"{respuesta[1]}")
        else:
            self.boton_cancelar = Button(master, text=" Cancelar ", bg="#DC324C", command=lambda:self.admin_cancelar(), width=10)
            self.boton_cancelar.grid(row=5, column=4,sticky='W')
            self.boton_guardar_cambio = Button(master, text=" Guardar ", bg="#4EDC32", command=lambda:self.admin_guardar_cambio(), width=10)
            self.boton_guardar_cambio.grid(row=5, column=3, sticky='W')
    
    def admin_guardar_cambio(self,):
        respuesta = self.obj.funcion_guardar_cambio(
                    self.tree, 
                    self.master, 
                    self.var_mail, 
                    self.var_nombre, 
                    self.var_apellido, 
                    self.var_sexo, 
                    self.var_preferencia
        )
        if respuesta[0] == '1':
            showinfo("Modificacion usuario", f"{respuesta[1]}")
            self.boton_cancelar.grid_forget()
            self.boton_guardar_cambio.grid_forget()
            self.boton_modificacion["state"]=NORMAL
            self.boton_grabar["state"]=NORMAL
            self.boton_consultar["state"]=NORMAL
            self.boton_eliminar["state"]=NORMAL
        else:
            showwarning("Modificacion usuario", f"{respuesta[1]}")

    def admin_cancelar(self,):
        blanqueo=Pantalla()
        self.boton_cancelar.grid_forget()
        self.boton_guardar_cambio.grid_forget()
        self.boton_modificacion["state"]=NORMAL
        self.boton_grabar["state"]=NORMAL
        self.boton_consultar["state"]=NORMAL
        self.boton_eliminar["state"]=NORMAL
        blanqueo.funcion_blanquear(self.tree,
                    self.var_mail, 
                    self.var_nombre, 
                    self.var_apellido, 
                    self.var_sexo, 
                    self.var_preferencia)