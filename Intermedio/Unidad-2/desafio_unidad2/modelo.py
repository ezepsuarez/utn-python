import sqlite3
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
from tkinter.messagebox import showwarning
from tkinter import DISABLED, NORMAL, font
from tkinter import Button
import re
from turtle import bgcolor, color 

mi_id=0

def conectar_base():
    #genera la conexion con sqlite
    con = sqlite3.connect('./bd_tp_final.db')
    return con

def funcion_grabar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
    con = conectar_base()
    #existe_tabla(con)
    #Esta funcion graba el alta de un usuario
    global mi_id
    resultado=funcion_validar_datos(var_mail, var_nombre, var_apellido)
    if (resultado != 1):
        mi_id += 1
        tree.insert("", "end", text=str(mi_id), values=(var_mail.get(), var_nombre.get(), var_apellido.get(), var_sexo.get(), var_preferencia.get()))
        cursor = con.cursor()
        data = (str(mi_id), var_mail.get(), var_nombre.get(), var_apellido.get(), var_sexo.get(), var_preferencia.get())
        sql = "INSERT INTO usuario(idusuario, mail, nombre, apellido, sexo, preferencia) VALUES(?,?, ?, ?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        funcion_blanquear(var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
        showinfo("Alta usuario", "Se registro un nuevo usuario")
    con.close

def funcion_validar_mail(var_mail):
    #valida que el mail este con el formato correcto usando regex.
    patron = re.compile(r"(<)?(\w+@\w+(?:\.[a-z]+)+)(?(1)>|$)", re.I)
    if (patron.search(var_mail.get())):
        return 0
    else:
        showwarning("Validacion Mail", "El email ingresado no esta en el formato esperado \nFormato: user@domino.com")
        return 1

def funcion_validar_datos(var_mail, var_nombre, var_apellido):
    #valida que todos los campos obligatorios sean ingresados y llama a la funcion que valida el formato de mail
    if (var_nombre.get() == "" or var_mail.get() == "" or var_apellido.get() == "" ):
        showwarning("Ingreso de datos", "Falta ingresar datos obligatorios\nDatos: [Email - Nombre - Apellido].")
        return 1

    if (funcion_validar_mail(var_mail) == 1):
        return 1

def existe_tabla(con):
    con = conectar_base()
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
    con = conectar_base()
    cursor = con.cursor()
    sql = "CREATE TABLE usuario(idusuario integer PRIMARY KEY, mail varchar(255) NOT NULL, nombre varchar(100) NOT NULL, apellido varchar(100) NOT NULL, sexo char(2), preferencia varchar(200))"
    cursor.execute(sql)
    con.commit()
    con.close
try:
    conectar_base()
    crear_tabla()
except:
    showwarning("Error", "Hubo un error al crear tabla")

def funcion_blanquear(var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
    #Esta funcion borra los campos en los textbox para evitar ingresar datos repetidos o luego de la modificacion que sigan apareciendo
    var_mail.set("")
    var_nombre.set("")
    var_apellido.set("")
    var_sexo.set("")
    var_preferencia.set("")

def funcion_consultar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
    con = conectar_base()
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

def funcion_eliminar(tree,var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
    con = conectar_base()
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
        funcion_blanquear(var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
        funcion_consultar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)

def funcion_modificar(tree, master, mail, nombre, apellido, sexo, preferencia, boton_eliminar, boton_grabar, boton_consultar, boton_modificacion):
    #modifica los datos del usuario
    global mi_id
    global boton_guardar_cambio
    global boton_cancelar
   
    item = tree.focus()
    if item == "" :
        showinfo("Seleccion", "Debe seleccionar un usuario a modificar")
    else:
        val=tree.item(item)['values'][0]
        print(f" el valor es {val}")

        mail.set(tree.item(item)['values'][0])
        nombre.set(tree.item(item)['values'][1])
        apellido.set(tree.item(item)['values'][2])
        sexo.set(tree.item(item)['values'][3])
        preferencia.set(tree.item(item)['values'][4])
        
        boton_eliminar["state"] = DISABLED
        boton_grabar["state"] = DISABLED
        boton_consultar["state"] = DISABLED
        boton_modificacion["state"] = DISABLED

        boton_cancelar= Button(master, text=" Cancelar ", bg="#DC324C", command=lambda:funcion_cancelar(mail, nombre, apellido, sexo, preferencia, master, boton_modificacion, boton_grabar, boton_consultar, boton_eliminar), width=10)
        boton_cancelar.grid(row=5, column=4,sticky="w")

        boton_guardar_cambio= Button(master, text=" Guardar ", bg="#4EDC32", command=lambda:funcion_guardar_cambio(tree, mail, nombre, apellido, sexo, preferencia, boton_modificacion,boton_grabar, boton_consultar, boton_eliminar), width=10)
        boton_guardar_cambio.grid(row=5, column=3, sticky="w")


def funcion_cancelar(mail, nombre, apellido, sexo, preferencia, boton_modificacion, boton_grabar, boton_consultar, boton_eliminar):
    #cancela la accion guardar al modificar
    funcion_blanquear(mail, nombre, apellido, sexo, preferencia)    
    global boton_guardar_cambio
    global boton_cancelar
    boton_cancelar.grid_forget()
    boton_guardar_cambio.grid_forget()
    boton_modificacion["state"]=NORMAL
    boton_grabar["state"]=NORMAL
    boton_consultar["state"]=NORMAL
    boton_eliminar["state"]=NORMAL

def funcion_guardar_cambio(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia, boton_modificacion, boton_grabar, boton_consultar, boton_eliminar):
    con = conectar_base()
    #Guarda los cambios luego de una modificacion
    global mi_id
    item = tree.focus()
    id=str((tree.item(item)['text'][0]))
    cursor = con.cursor()
    resultado=funcion_validar_datos(var_mail, var_nombre, var_apellido)
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
        funcion_blanquear(var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
        funcion_consultar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)

#existe_tabla(conectar_base)