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

def funcion_validar_mail():
    #valida que el mail este con el formato correcto usando regex.
    patron = re.compile(r"(<)?(\w+@\w+(?:\.[a-z]+)+)(?(1)>|$)", re.I)
    mail = var_mail.get()
    if (patron.search(mail)):
        return 0
    else:
        showwarning("Validacion Mail", "El email ingresado no esta en el formato esperado \nFormato: user@domino.com")
        return 1

def conectar_base():
    #genera la conexion con sqlite
    con = sqlite3.connect('bd_tp_final.db')
    return con

def funcion_validar_datos():
    #valida que todos los campos obligatorios sean ingresados y llama a la funcion que valida el formato de mail
    if (var_nombre.get() == "" or var_mail.get() == "" or var_apellido.get() == "" ):
        showwarning("Ingreso de datos", "Falta ingresar datos obligatorios\nDatos: [Email - Nombre - Apellido].")
        return 1

    if (funcion_validar_mail() == 1):
        return 1

def existe_tabla(con):
    #sino existe la tabla la crea, para evitar que genere un error por existencia de la tabla
    cursor = con.cursor()
    sql= "SELECT * FROM sqlite_master where type='table' and name='usuario'"
    cursor.execute(sql)
    con.commit()
    con.close
    rows = cursor.fetchall()
    if len(rows) == 0:
        crear_tabla(con)

def crear_tabla(con):
    #crea la tabla usuarios
    cursor = con.cursor()
    sql = "CREATE TABLE usuario(idusuario integer PRIMARY KEY, mail varchar(255) NOT NULL, nombre varchar(100) NOT NULL, apellido varchar(100) NOT NULL, sexo char(2), preferencia varchar(200))"
    cursor.execute(sql)
    con.commit()
    con.close

def funcion_blanquear():
    #Esta funcion borra los campos en los textbox para evitar ingresar datos repetidos o luego de la modificacion que sigan apareciendo
    var_mail.set("")
    var_nombre.set("")
    var_apellido.set("")
    var_sexo.set("")
    var_preferencia.set("")

def funcion_grabar():
    #Esta funcion graba el alta de un usuario
    global mi_id
    resultado=funcion_validar_datos()
    if (resultado != 1):
        mi_id += 1
        tree.insert("", "end", text=str(mi_id), values=(var_mail.get(), var_nombre.get(), var_apellido.get(), var_sexo.get(), var_preferencia.get()))
        print(f"Id: {mi_id} - Email: {var_mail.get()}  - Nombre: {var_nombre.get()} - Apellido: {var_apellido.get()} - Sexo: {var_sexo.get()}- Preferencia: {var_preferencia.get()}")
        cursor = con.cursor()
        data = (str(mi_id), var_mail.get(), var_nombre.get(), var_apellido.get(), var_sexo.get(), var_preferencia.get())
        sql = "INSERT INTO usuario(idusuario, mail, nombre, apellido, sexo, preferencia) VALUES(?,?, ?, ?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        con.close
        funcion_blanquear()
        showinfo("Alta usuario", "Se registro un nuevo usuario")

def funcion_consultar():
    #Esta funcion permite hacer consulta de los registros en la base de datos
    #Vaciamos la grilla con los resultados
    for row in tree.get_children():
            tree.delete(row)
    cursor = con.cursor()
    #Sino se ingresan datos en la busqueda trae todo los datos
    if (var_nombre.get() == "" and var_mail.get() == "" and var_apellido.get() == "" and var_sexo.get() == "" and var_preferencia.get() == "" ):
        sql = "SELECT * FROM usuario"
    else:
        sql = "SELECT * FROM usuario WHERE mail = '" + var_mail.get() + "' OR nombre = '" + var_nombre.get() + "' OR apellido = '" + var_apellido.get() + "' OR sexo = '" + var_sexo.get() + "' OR preferencia = '" + var_preferencia.get() + "' "
    
    cursor.execute(sql)
    con.commit()
    con.close
    rows = cursor.fetchall()

    #Mostramos los resultados
    if len(rows) == 0:
        showinfo("Busqueda", "No se encontro un resultado")

    for row in rows:
        tree.insert("", "end", text=str(row[0]), values=(row[1], row[2], row[3], row[4], row[5]))

def funcion_eliminar():
    #elimina un usuario seleccionado, sino se selecciona un usuario muestra una alerta
    global mi_id
    item = tree.focus()
   
    if item == "" :
        showwarning("Seleccion", "Debe seleccion un usuario")
    elif askyesno("Eliminacion de usuario", "Esta por eliminar este usuario, desea continuar?"):
        id_borrar=(tree.item(item)['text'][0])
        tree.delete(item)
        cursor = con.cursor()
        data = (id_borrar)
        sql = "DELETE from usuario where idusuario = ?;"
        cursor.execute(sql, data)
        con.commit()
        con.close
        showinfo("Eliminacion", "Se elimino el usuario")
        mi_id -= 1
        funcion_blanquear()
        funcion_consultar()

def funcion_modificar():
    #modifica los datos del usuario
    global mi_id
    global boton_guardar_cambio
    global boton_cancelar
    item = tree.focus()

    if item == "" :
        showinfo("Seleccion", "Debe seleccionar un usuario a modificar")
    else:
        var_mail.set(tree.item(item)['values'][0])
        var_nombre.set(tree.item(item)['values'][1])
        var_apellido.set(tree.item(item)['values'][2])
        var_sexo.set(tree.item(item)['values'][3])
        var_preferencia.set(tree.item(item)['values'][4])
        

        boton_eliminar["state"] = DISABLED
        boton_grabar["state"] = DISABLED
        boton_consultar["state"] = DISABLED
        boton_modificacion["state"] = DISABLED

        boton_cancelar= Button(master, text=" Cancelar ", bg="#DC324C", command=funcion_cancelar, width=10)
        boton_cancelar.grid(row=5, column=4,sticky=W)

        boton_guardar_cambio= Button(master, text=" Guardar ", bg="#4EDC32", command=funcion_guardar_cambio, width=10)
        boton_guardar_cambio.grid(row=5, column=3, sticky=W)

def funcion_cancelar():
    #cancela la accion guardar al modificar
    funcion_blanquear()
    boton_cancelar.grid_forget()
    boton_guardar_cambio.grid_forget()
    boton_modificacion["state"]=NORMAL
    boton_grabar["state"]=NORMAL
    boton_consultar["state"]=NORMAL
    boton_eliminar["state"]=NORMAL

def funcion_guardar_cambio():
    #Guarda los cambios luego de una modificacion
    global mi_id
    item = tree.focus()
    id=str((tree.item(item)['text'][0]))
    cursor = con.cursor()
    resultado=funcion_validar_datos()
    if (resultado != 1):
        sql = "UPDATE usuario SET mail='" + var_mail.get() + "', nombre='" + var_nombre.get() + "', apellido= '" + var_apellido.get() + "', sexo= '" + var_sexo.get() + "', preferencia = '" + var_preferencia.get() + "'WHERE idusuario= '" + id + "';"
        cursor.execute(sql)
        con.commit()
        con.close
        showinfo("Actualizacion", "Se han actualizado los datos")
        boton_cancelar.grid_forget()
        boton_guardar_cambio.grid_forget()
        boton_modificacion["state"]=NORMAL
        boton_grabar["state"]=NORMAL
        boton_consultar["state"]=NORMAL
        boton_eliminar["state"]=NORMAL
        funcion_blanquear()
        funcion_consultar()

con = conectar_base()       
#Valida si existe la tabla usuarios, sino la crea
existe_tabla(con)

boton_grabar =Button(master, text=" Alta ", bg="#326DDC", command=funcion_grabar, width=10)
boton_grabar.grid(row=3, column=3, sticky=W)

boton_eliminar= Button(master, text=" Baja ", bg="#DC3232", command=funcion_eliminar, width=10)
boton_eliminar.grid(row=4, column=3,sticky=W)

boton_consultar= Button(master, text=" Consulta ", bg="grey", command=funcion_consultar, width=10)
boton_consultar.grid(row=3, column=4,sticky=W)

boton_modificacion= Button(master, text=" Modificar", bg="grey", command=funcion_modificar, width=10)
boton_modificacion.grid(row=4, column=4,sticky=W)

master.mainloop()