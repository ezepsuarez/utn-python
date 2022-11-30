## Aplicacion realizada por:
## Cesar Mariño
## Guido Mariano Gonzalez
## Valentino Oliva Gilardi 
## Ezequiel Suarez

from cProfile import label
from cgitb import enable
from queue import Empty
from tkinter import * 
from tkinter import ttk
import sqlite3
from tkinter import font
from tkinter.tix import Tree
from tkinter.messagebox import *
import re
from turtle import bgcolor, color 
import modelo

mi_id=0
master = Tk()

master.title("Aplicacion Entrega Final")

#Centramos la ventana
width = 660 # Width 
height = 510 # Height
screen_width = master.winfo_screenwidth()  # Width of the screen
screen_height = master.winfo_screenheight() # Height of the screen
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
master.geometry('%dx%d+%d+%d' % (width, height, x, y))

#Ponemos titulo
titulo = Label(master, bd="10",fg="white" ,text="AMB de usuarios", width=100)
titulo.grid(row=0, column=0, columnspan=6)
titulo.config(bg="grey")

var_mail= StringVar()
var_nombre= StringVar()
var_apellido = StringVar()
var_preferencia= StringVar()
var_sexo=StringVar()

mail = Label(master, text="Email :")
mail.grid(row=2, column=1, sticky=W)

nombre = Label(master, text="Nombre :")
nombre.grid(row=3, column=1, sticky=W)

apellido = Label(master, text="Apellido :")
apellido.grid(row=4, column=1, sticky=W)

sexo = Label(master, text="Sexo :")
sexo.grid(row=5, column=1, sticky=W)

preferencia = Label(master, text="Preferencia :")
preferencia.grid(row=6, column=1, sticky=W)

mail = Entry(master, textvariable=var_mail, width=30)
mail.grid (row=2, column=2,sticky=W)

nombre = Entry(master, textvariable=var_nombre, width=30)
nombre.grid (row=3, column=2,sticky=W)

apellido = Entry(master, textvariable=var_apellido, width=30)
apellido.grid (row=4, column=2,sticky=W)

sexo = Entry(master, textvariable=var_sexo, width=30)
sexo.grid (row=5, column=2,sticky=W)

preferencia = Entry(master, textvariable=var_preferencia, width=30)
preferencia.grid (row=6, column=2,sticky=W)

tree = ttk.Treeview(master,height=15)
tree['columns'] = ("col1", "col2", "col3", "col4", "col5")
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.heading("#0", text="ID")
tree.column("col1", width=180, minwidth=180, anchor=W)
tree.heading("col1", text="Email")
tree.column("col2", width=80, minwidth=80, anchor=W)
tree.heading("col2", text="Nombre")
tree.column("col3", width=100, minwidth=100, anchor=W)
tree.heading("col3", text="Apellido")
tree.column("col4", width=70, minwidth=70, anchor=W)
tree.heading("col4", text="Sexo")
tree.column("col5", width=100, minwidth=100, anchor=W)
tree.heading("col5", text="Preferencia")
tree.grid(row=12, column=0, columnspan=5)


boton_grabar =Button(master, text=" Alta ", bg="#326DDC", command=lambda: modelo.funcion_grabar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia), width=10)
boton_grabar.grid(row=3, column=3, sticky=W)

boton_eliminar= Button(master, text=" Baja ", bg="#DC3232", command=lambda: modelo.funcion_eliminar(tree,var_mail, var_nombre, var_apellido, var_sexo, var_preferencia), width=10)
boton_eliminar.grid(row=4, column=3,sticky=W)

boton_consultar= Button(master, text=" Consulta ", bg="grey", command=lambda: modelo.funcion_consultar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia), width=10)
boton_consultar.grid(row=3, column=4,sticky=W)

boton_modificacion= Button(master, text=" Modificar", bg="grey", command=lambda: modelo.funcion_modificar(tree, master, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia, boton_eliminar,boton_grabar,boton_consultar,boton_modificacion), width=10)
boton_modificacion.grid(row=4, column=4,sticky=W)

master.mainloop()