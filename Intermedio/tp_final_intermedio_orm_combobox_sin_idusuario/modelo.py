from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
from tkinter.messagebox import showwarning
from tkinter import DISABLED, NORMAL, font
from tkinter import Button
import re
from turtle import bgcolor, color 
from peewee import *
import os
import datetime

db = SqliteDatabase("bd_tp_final_intermedio.db")


class BaseModel(Model):
    class Meta:
        database = db


class Usuario(BaseModel):
    mail = CharField(unique=True)
    nombre = CharField()
    apellido = CharField()
    sexo = FixedCharField()
    preferencia = IntegerField()


class Categoria(BaseModel):
    descripcion_categoria = CharField(unique=True)


db.connect()
db.create_tables([Usuario])
db.create_tables([Categoria])


class RegistroLogError(Exception):

    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    ruta = os.path.join(BASE_DIR, "log_abm_usuario.txt")

    def __init__(self, linea, archivo, fecha):
        self.linea = linea
        self.archivo = archivo
        self.fecha = fecha

    def registrar_error(self, error):
        log = open(self.ruta, "a")
        self.error = error
        print(self.fecha, "- ERROR - ", self.archivo, self.linea, f"Detalle Error: {self.error}", file=log)


class Persona():
    def __init__(self, mail, nombre, apellido, sexo, preferencia):
        self.mail = mail
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.preferencia = preferencia


class Abm():
    def funcion_grabar(self, tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
        datospersona = Persona(var_mail.get(), var_nombre.get(), var_apellido.get(), var_sexo.get(), var_preferencia.get())
        resultado = Validacion()
        valor = resultado.funcion_validar_datos(datospersona.mail, datospersona.nombre, datospersona.apellido)
        if (valor != 1):
            try:                
                usuario = Usuario()
                usuario.mail = datospersona.mail
                usuario.nombre = datospersona.nombre
                usuario.apellido = datospersona.apellido
                usuario.sexo = datospersona.sexo
                usuario.preferencia = datospersona.preferencia
                usuario.save()
                tree.insert("", "end", text="", values=(datospersona.mail, datospersona.nombre, datospersona.apellido, datospersona.sexo, datospersona.preferencia))
                blanqueo = Pantalla()
                blanqueo.funcion_blanquear(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
                showinfo("Alta usuario", "Se registro un nuevo usuario")
            #except IntegrityError as err:
            except Exception as err:
                log = RegistroLogError("Error al registrar usuario","modelo.py->linea 75", datetime.datetime.now())
                log.registrar_error(err)
                showwarning("error", f"Error: {err}")

    def poblar_categoria(self,):
        lista_categoria = ['Viajes','Moda','Motos','Autos','Noticias','Juegos','Deportes','Comidas','Compras']
        for x in lista_categoria:
            categoria = Categoria()
            categoria.descripcion_categoria = x
            try:
                categoria.save()
            except Exception as err:
                log = RegistroLogError("Error al cargar categorias","modelo.py->linea 87",datetime.datetime.now())
                log.registrar_error(err)

    def carga_categoria(self,):
        categoria = Categoria.select()
        if len(categoria) == 0:
            self.poblar_categoria()
            categoria = Categoria.select()
        return categoria

    def dar_id_categoria(self, categoriabuscada):
        sql = Categoria.select().where((Categoria.descripcion_categoria == categoriabuscada))
        return sql

    def funcion_consultar(self, tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
        for row in tree.get_children():
            tree.delete(row)
        if (var_nombre.get() == "" and var_mail.get() == "" and var_apellido.get() == "" and var_sexo.get() == "" and var_preferencia.get() == "" ):
            sql = (Usuario.select( Usuario.mail, Usuario.nombre, Usuario.apellido, Usuario.sexo, Categoria.id.alias('id'), Categoria.descripcion_categoria.alias('preferencia')).join(Categoria, on=(Usuario.preferencia == Categoria.id)).objects())
        else:
            sql = Usuario.select().where( (Usuario.mail == var_mail.get()) | (Usuario.nombre == var_nombre.get()) | (Usuario.apellido == var_apellido.get()) | (Usuario.sexo == var_sexo.get()) | (Usuario.preferencia == var_preferencia.get()))
        if len(sql) == 0:
            showinfo("Busqueda", "No se encontro un resultado")
        for row in sql:
            tree.insert("", "end", text=row.mail, values=(row.nombre, row.apellido, row.sexo, row.preferencia))

    def funcion_eliminar(self, tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
        item = tree.focus()
        if (item == ""):
            showwarning("Seleccion", "Debe seleccion un usuario")
        elif askyesno("Eliminacion de usuario", "Esta por eliminar este usuario, desea continuar?"):
            id = tree.item(item)['text']
            tree.delete(item)
            try:
                borrar = Usuario.get(Usuario.mail == id)
                borrar.delete_instance()
                showinfo("Eliminacion", "Se elimino el usuario")
                pantalla = Pantalla()
                pantalla.funcion_blanquear(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
                self.funcion_consultar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
            except Exception as err:
                log = RegistroLogError("Error al eliminar un usuario","modelo.py->linea 125",datetime.datetime.now())
                log.registrar_error(err)

    def funcion_modificar(self, tree, master, mail, nombre, apellido, sexo, preferencia, boton_eliminar, boton_grabar, boton_consultar, boton_modificacion):
        global boton_guardar_cambio
        global boton_cancelar
        item = tree.focus()
        if item == "":
            showinfo("Seleccion", "Debe seleccionar un usuario a modificar")
        else:
            mail.set(tree.item(item)['text'])
            nombre.set(tree.item(item)['values'][0])
            apellido.set(tree.item(item)['values'][1])
            sexo.set(tree.item(item)['values'][2])
            aux = tree.item(item)['values'][3] 
            sql = self.dar_id_categoria(aux)
            for row in sql:
                aux = row.id
            preferencia.set(aux)
            boton = Pantalla()
            boton_eliminar["state"] = DISABLED
            boton_grabar["state"] = DISABLED
            boton_consultar["state"] = DISABLED
            boton_modificacion["state"] = DISABLED
            boton_cancelar = Button(master, text=" Cancelar ", bg="#DC324C", command=lambda:boton.funcion_cancelar(tree, mail, nombre, apellido, sexo, preferencia, boton_modificacion, boton_grabar, boton_consultar, boton_eliminar), width=10)
            boton_cancelar.grid(row=5, column=4,sticky='W')
            boton_guardar_cambio = Button(master, text=" Guardar ", bg="#4EDC32", command=lambda:self.funcion_guardar_cambio(tree, master, mail, nombre, apellido, sexo, preferencia, boton_modificacion,boton_grabar, boton_consultar, boton_eliminar), width=10)
            boton_guardar_cambio.grid(row=5, column=3, sticky='W')

    def funcion_guardar_cambio(self, tree, master, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia, boton_modificacion, boton_grabar, boton_consultar, boton_eliminar):
        item = tree.focus()
        id = tree.item(item)['text']
        datospersona = Persona(var_mail.get(), var_nombre.get(), var_apellido.get(), var_sexo.get(), var_preferencia.get())
        valor = Validacion()
        resultado = valor.funcion_validar_datos(datospersona.mail, datospersona.nombre, datospersona.apellido)
        if (resultado != 1):
            actualizar = Usuario.update(mail=datospersona.mail, nombre=datospersona.nombre, apellido=datospersona.apellido, sexo=datospersona.sexo, preferencia=datospersona.preferencia).where(Usuario.mail==id)
            try:
                actualizar.execute()
                showinfo("Actualizacion", "Se han actualizado los datos")
                boton_cancelar.grid_forget()
                boton_guardar_cambio.grid_forget()
                boton_modificacion["state"]=NORMAL
                boton_grabar["state"]=NORMAL
                boton_consultar["state"]=NORMAL
                boton_eliminar["state"]=NORMAL
                pantalla = Pantalla()
                pantalla.funcion_blanquear(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
                self.funcion_consultar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
            except Exception as err:
                log = RegistroLogError("Error al actualizar datos de usuarios","modelo.py->linea 166",datetime.datetime.now())
                log.registrar_error(err)


class Validacion():
    def funcion_validar_nombre(self, nombre):
        patron = re.compile(r"^[A-Za-z]+(?:[ _-][A-Za-z]+)*$", re.I)
        if (patron.search(nombre)):
            return 0
        else:
            showwarning("Validacion Nombre", "El nombre ingresado no puede contener numeros")
            return 1

    def funcion_validar_mail(self, mail):
        patron = re.compile(r"(<)?(\w+@\w+(?:\.[a-z]+)+)(?(1)>|$)", re.I)
        if (patron.search(mail)):
            return 0
        else:
            showwarning("Validacion Mail", "El email ingresado no esta en el formato esperado \nFormato: user@domino.com")
            return 1

    def funcion_validar_datos(self, mail, nombre, apellido):
        if (nombre == "" or mail == "" or apellido == "" ):
            showwarning("Ingreso de datos", "Falta ingresar datos obligatorios\nDatos: [Email - Nombre - Apellido].")
            return 1
        if (self.funcion_validar_mail(mail) == 1):
            return 1
        if (self.funcion_validar_nombre(nombre) == 1):
            return 1


class Pantalla():
    def funcion_blanquear(self, tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
        var_mail.set("")
        var_nombre.set("")
        var_apellido.set("")
        var_sexo.set("")
        var_preferencia.set("")
        consulta = Abm()
        consulta.funcion_consultar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)

    def funcion_cancelar(self, tree, mail, nombre, apellido, sexo, preferencia, boton_modificacion, boton_grabar, boton_consultar, boton_eliminar):
        self.funcion_blanquear(tree, mail, nombre, apellido, sexo, preferencia)   
        global boton_guardar_cambio
        global boton_cancelar
        boton_cancelar.grid_forget()
        boton_guardar_cambio.grid_forget()
        boton_modificacion["state"]=NORMAL
        boton_grabar["state"]=NORMAL
        boton_consultar["state"]=NORMAL
        boton_eliminar["state"]=NORMAL