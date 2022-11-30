from pickle import FALSE
import sqlite3
from sre_parse import State
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
from tkinter.messagebox import showwarning
from tkinter import DISABLED, NORMAL, font
from tkinter import Button
import re
from turtle import bgcolor, color 
from peewee import *

mi_id=0

db = SqliteDatabase("bd_tp_final_intermedio.db")

class BaseModel(Model):
    class Meta:
        database = db

class Usuario(BaseModel):
    idusuario = IntegerField(unique=True)
    mail = CharField()
    nombre = CharField()
    apellido = CharField()
    sexo = FixedCharField()
    preferencia = CharField()


db.connect()
db.create_tables([Usuario])

class Persona():
    def __init__(self, mail, nombre, apellido, sexo, preferencia):
        self.mail = mail
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.preferencia = preferencia

class Abm():
    def funcion_grabar(self, tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
        datospersona=Persona(var_mail.get(), var_nombre.get(), var_apellido.get(), var_sexo.get(), var_preferencia.get())
        #Esta funcion graba el alta de un usuario
        global mi_id
        resultado=Validacion()
        valor=resultado.funcion_validar_datos(datospersona.mail, datospersona.nombre, datospersona.apellido)
        if (valor != 1):
            mi_id += 1
            try:                
                usuario=Usuario()
                usuario.idusuario=mi_id
                usuario.mail=datospersona.mail
                usuario.nombre=datospersona.nombre
                usuario.apellido=datospersona.apellido
                usuario.sexo=datospersona.sexo
                usuario.preferencia=datospersona.preferencia
                usuario.save()
                tree.insert("", "end", text=str(mi_id), values=(datospersona.mail, datospersona.nombre, datospersona.apellido, datospersona.sexo, datospersona.preferencia))
                blanqueo=Pantalla()
                blanqueo.funcion_blanquear(var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
                showinfo("Alta usuario", "Se registro un nuevo usuario")
            except:
                showwarning("Alta usuario", "Error al registrar usuario")

    def funcion_consultar(self, tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
        #Esta funcion permite hacer consulta de los registros en la base de datos
        #Vaciamos la grilla con los resultados
        for row in tree.get_children():
            tree.delete(row)
        
        #Sino se ingresan datos en la busqueda trae todo los datos
        if (var_nombre.get() == "" and var_mail.get() == "" and var_apellido.get() == "" and var_sexo.get() == "" and var_preferencia.get() == "" ):
            sql = Usuario.select()
        else:
            sql = Usuario.select().where( (Usuario.mail==var_mail.get()) | (Usuario.nombre == var_nombre.geta()) | (Usuario.apellido == var_apellido.get()) | (Usuario.sexo == var_sexo.get()) | (Usuario.preferencia == var_preferencia.get()))
        #Mostramos los resultados
        if len(sql) == 0:
            showinfo("Busqueda", "No se encontro un resultado")
        for row in sql:
            tree.insert("", "end", text=str(row.idusuario), values=(row.mail, row.nombre, row.apellido, row.sexo, row.preferencia))

    def funcion_eliminar(self, tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
        #elimina un usuario seleccionado, sino se selecciona un usuario muestra una alerta
        global mi_id
        item = tree.focus()
        if item == "" :
            showwarning("Seleccion", "Debe seleccion un usuario")
        elif askyesno("Eliminacion de usuario", "Esta por eliminar este usuario, desea continuar?"):
            id_borrar=(tree.item(item)['text'][0])
            tree.delete(item)
            try:
                borrar=Usuario.get(Usuario.idusuario==id_borrar)
                borrar.delete_instance()
                showinfo("Eliminacion", "Se elimino el usuario")
                mi_id -= 1
                pantalla=Pantalla()
                pantalla.funcion_blanquear(var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
                self.funcion_consultar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
            except sqlite3.Error as er:
                print(f'Excepción: {er}')

    def funcion_modificar(self, tree, master, mail, nombre, apellido, sexo, preferencia, boton_eliminar, boton_grabar, boton_consultar, boton_modificacion):
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

            boton=Pantalla()
            boton_eliminar["state"] = DISABLED
            boton_grabar["state"] = DISABLED
            boton_consultar["state"] = DISABLED
            boton_modificacion["state"] = DISABLED
            boton_cancelar= Button(master, text=" Cancelar ", bg="#DC324C", command=lambda:boton.funcion_cancelar(mail, nombre, apellido, sexo, preferencia, master, boton_modificacion, boton_grabar, boton_consultar, boton_eliminar), width=10)
            boton_cancelar.grid(row=5, column=4,sticky='W')
            boton_guardar_cambio= Button(master, text=" Guardar ", bg="#4EDC32", command=lambda:self.funcion_guardar_cambio(tree, master, mail, nombre, apellido, sexo, preferencia, boton_modificacion,boton_grabar, boton_consultar, boton_eliminar), width=10)
            boton_guardar_cambio.grid(row=5, column=3, sticky='W')

    def funcion_guardar_cambio(self, tree, master, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia, boton_modificacion, boton_grabar, boton_consultar, boton_eliminar):
        #Guarda los cambios luego de una modificacion
        global mi_id
        item = tree.focus()
        id=str((tree.item(item)['text'][0]))
        datospersona=Persona(var_mail.get(), var_nombre.get(), var_apellido.get(), var_sexo.get(), var_preferencia.get())
        print("que hay aca", datospersona.nombre)
        valor=Validacion()
        resultado=valor.funcion_validar_datos(datospersona.mail, datospersona.nombre, datospersona.apellido)
        if (resultado != 1):
            actualizar = Usuario.update(mail=datospersona.mail,  nombre=datospersona.nombre, apellido=datospersona.apellido, sexo=datospersona.sexo, preferencia=datospersona.preferencia).where(Usuario.idusuario==id)
            actualizar.execute()
            showinfo("Actualizacion", "Se han actualizado los datos")
            boton_cancelar.grid_forget()
            boton_guardar_cambio.grid_forget()
            boton_modificacion["state"]=NORMAL
            boton_grabar["state"]=NORMAL
            boton_consultar["state"]=NORMAL
            boton_eliminar["state"]=NORMAL
            pantalla=Pantalla()
            pantalla.funcion_blanquear(var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
            self.funcion_consultar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)

class Validacion():

    def funcion_validar_nombre(self, nombre):
        print("el nombre: ", nombre)
        patron= re.compile(r"^[A-Za-z]+(?:[ _-][A-Za-z]+)*$", re.I)
        if (patron.search(nombre)):
            return 0
        else:
            showwarning("Validacion Nombre", "El nombre ingresado no puede contener numeros")
            return 1
        
    def funcion_validar_mail(self, mail):
        #valida que el mail este con el formato correcto usando regex.
        print("el mail:", mail)
        patron = re.compile(r"(<)?(\w+@\w+(?:\.[a-z]+)+)(?(1)>|$)", re.I)
        if (patron.search(mail)):
            return 0
        else:
            showwarning("Validacion Mail", "El email ingresado no esta en el formato esperado \nFormato: user@domino.com")
            return 1

    def funcion_validar_datos(self, mail, nombre, apellido):
        #valida que todos los campos obligatorios sean ingresados y llama a la funcion que valida el formato de mail
        if (nombre== "" or mail == "" or apellido == "" ):
            showwarning("Ingreso de datos", "Falta ingresar datos obligatorios\nDatos: [Email - Nombre - Apellido].")
            return 1
        if (self.funcion_validar_mail(mail) == 1):
            return 1
        if (self.funcion_validar_nombre(nombre) == 1):
                return 1

class Pantalla():
    def funcion_blanquear(self, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
        #Esta funcion borra los campos en los textbox para evitar ingresar datos repetidos o luego de la modificacion que sigan apareciendo
        var_mail.set("")
        var_nombre.set("")
        var_apellido.set("")
        var_sexo.set("")
        var_preferencia.set("")

    def funcion_cancelar(self, master, mail, nombre, apellido, sexo, preferencia):
        #cancela la accion guardar al modificar
        self.funcion_blanquear(mail, nombre, apellido, sexo, preferencia)   
        global boton_guardar_cambio
        global boton_cancelar
        boton_cancelar.grid_forget()
        boton_guardar_cambio.grid_forget()
        boton_modificacion["state"]=NORMAL
        boton_grabar["state"]=NORMAL
        boton_consultar["state"]=NORMAL
        boton_eliminar["state"]=NORMAL 

