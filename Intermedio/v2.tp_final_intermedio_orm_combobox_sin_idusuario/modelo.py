from tkinter.messagebox import askyesno
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
        respuesta = resultado.funcion_validar_datos(datospersona.mail, datospersona.nombre, datospersona.apellido, datospersona.sexo, datospersona.preferencia)
        if respuesta[0] == '1':
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
                return ['1','Se registro un nuevo usuario']
            except Exception as err:
                log = RegistroLogError("Error al registrar usuario","modelo.py->linea 75", datetime.datetime.now())
                log.registrar_error(err)
                return ['0',f'{err}']
        else:
            return [respuesta[0], respuesta[1]]

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
            sql = Usuario.select().where( (Usuario.mail == var_mail.get()) | (Usuario.nombre == var_nombre.get()) | (Usuario.apellido == var_apellido.get()))

        if len(sql) == 0:
            return ['0',"No se encontro un resultado"]
        else:
            for row in sql:
                tree.insert("", "end", text=row.mail, values=(row.nombre, row.apellido, row.sexo, row.preferencia))
            return ['1','OK']

    def funcion_eliminar(self, tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
        item = tree.focus()
        if (item == ""):
            return ['2','Debe seleccion un usuario a eliminar']
        elif askyesno("Eliminacion de usuario", "Esta por eliminar este usuario, desea continuar?"):
            id = tree.item(item)['text']
            tree.delete(item)
            try:
                borrar = Usuario.get(Usuario.mail == id)
                borrar.delete_instance()
                pantalla = Pantalla()
                pantalla.funcion_blanquear(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
                self.funcion_consultar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
                return ['1','Se elimino el usuario']
            except Exception as err:
                log = RegistroLogError("Error al eliminar un usuario","modelo.py->linea 125",datetime.datetime.now())
                log.registrar_error(err)
                return ['0',f'{err}']

    def funcion_modificar(self, tree, master, mail, nombre, apellido, sexo, preferencia):
        item = tree.focus()
        if item == "":
            return ['2','Debe seleccion un usuario a modificar']
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
            return ['0','ok']

    def funcion_guardar_cambio(self, tree, master, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
        item = tree.focus()
        id = tree.item(item)['text']
        datospersona = Persona(var_mail.get(), var_nombre.get(), var_apellido.get(), var_sexo.get(), var_preferencia.get())
        valor = Validacion()
        respuesta = valor.funcion_validar_datos(datospersona.mail, datospersona.nombre, datospersona.apellido, datospersona.sexo, datospersona.preferencia)
        if respuesta[0] == '1':
            try:
                actualizar = Usuario.update(mail=datospersona.mail, nombre=datospersona.nombre, apellido=datospersona.apellido, sexo=datospersona.sexo, preferencia=datospersona.preferencia).where(Usuario.mail==id)
                actualizar.execute()
                pantalla = Pantalla()
                pantalla.funcion_blanquear(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
                self.funcion_consultar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
                return ['1',"Se han actualizado los datos"]
            except Exception as err:
                log = RegistroLogError("Error al actualizar datos de usuarios","modelo.py->linea 166",datetime.datetime.now())
                log.registrar_error(err)
                return ['0',f'{err}']
        else:
            return [respuesta[0], respuesta[1]]

class Validacion():
    def funcion_validar_nombre(self, nombre):
        patron = re.compile(r"^[A-Za-z]+(?:[ _-][A-Za-z]+)*$", re.I)
        if (patron.search(nombre)):
            return ['1','OK']
        else:
            return ['3','El nombre ingresado no puede contener numeros']

    def funcion_validar_mail(self, mail):
        patron = re.compile(r"(<)?(\w+@\w+(?:\.[a-z]+)+)(?(1)>|$)", re.I)
        if (patron.search(mail)):
            return ['1','OK']
        else:
            return ['3', 'El email ingresado no esta en el formato esperado \nFormato: user@domino.com']

    def funcion_validar_datos(self, mail, nombre, apellido, sexo, preferencia):
        if (nombre == "" or mail == "" or apellido == "" or sexo == "" or preferencia == "" ):
            return ['3','Falta ingresar datos obligatorios\n Datos obligatorios: [Email - Nombre - Apellido - Sexo - Preferencia].']
        else:  
            if (self.funcion_validar_mail(mail)[0] != '1'):
                return ['3','El main ingresado esta en formato invalido, debe ser usuario@dominio.com']
            else:           
                if (self.funcion_validar_nombre(nombre)[0] != '1'):
                    return ['3','El nombre no puede contener numeros']
                else:
                    return ['1','OK']


class Pantalla():
    def funcion_blanquear(self, tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
        var_mail.set("")
        var_nombre.set("")
        var_apellido.set("")
        var_sexo.set("")
        var_preferencia.set("")
        consulta = Abm()
        consulta.funcion_consultar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)