from tkinter import * 
from tkinter import ttk
import sqlite3

diccio={}
mi_id=0

master = Tk()

var_titulo= StringVar()
var_ruta= StringVar()
var_descripcion = StringVar()

titulo = Label(master, text="Titulo :")
titulo.grid(row=1, column=1, sticky=W)

ruta = Label(master, text="ruta :")
ruta.grid(row=2, column=1, sticky=W)


descripcion = Label(master, text="Descripcion :")
descripcion.grid(row=3, column=1, sticky=W)


titulo = Entry(master, textvariable=var_titulo, width=30)
titulo.grid (row=1, column=2,sticky=W)

ruta = Entry(master, textvariable=var_ruta, width=30)
ruta.grid (row=2, column=2,sticky=W)

descripcion = Entry(master, textvariable=var_descripcion, width=30)
descripcion.grid (row=3, column=2,sticky=W)

def conectar_base():
    con = sqlite3.connect('bd_desafio_unidad_6.db')
    return con

def crear_tabla(con):

    cursor = con.cursor()
    sql = "CREATE TABLE personas(id integer PRIMARY KEY, titulo text, ruta text, descripcion text)"
    cursor.execute(sql)
    con.commit()

def funcion_grabar():
    global mi_id
    mi_id += 1
    print(f"titulo: {var_titulo.get()}  - ruta: {var_ruta.get()} - descripcion: {var_descripcion.get()}")
    cursor = con.cursor()
    mi_id = int(mi_id)
    data = (mi_id, var_titulo.get(), var_ruta.get(), var_descripcion.get())
    sql = "INSERT INTO personas(id, titulo, ruta, descripcion) VALUES(?, ?, ?, ?)"
    cursor.execute(sql, data)
    con.commit()

def funcion_sorpresa():
    print("sorpresa")
    master.configure(bg='red')

con = conectar_base()
crear_tabla(con)

boton_grabar =Button(master, text="Alta", command=funcion_grabar)
boton_grabar.grid(row=5, column=2, sticky=W)

boton_eliminar= Button(master, text="Sorpresa", command=funcion_sorpresa)
boton_eliminar.grid(row=5, column=3,sticky=W)

master.mainloop()