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

mi_id=0

class BotonB:
    def __init__(self, parent=None, *args,**kwars):
        self.master=parent
        self.drow=kwars.get('drow')
        self.dcol=kwars.get('dcol')
        self.dsti=kwars.get('dsti')
        self.text=kwars.get('text')
        self.command=kwars.get('command')
        self.width=kwars.get('width')
        self.bgcolor=kwars.get('bg')
        self.bstate=kwars.get('state')
        self.ocultar=kwars.get('ocultar')
        print(f"Row es --> {self.drow} ---- Col es ---> {self.dcol} ---- Sticky ---> {self.dsti}")

        self.b1=Button(self.master, text=self.text, command=self.command, state=self.bstate, width=self.width)
        self.b1.grid(row=self.drow, column=self.dcol, sticky=self.dsti)
        self.b1.config(command=self.command, bg=self.bgcolor)            

class Persona():
    def __init__(self, mail, nombre, apellido, sexo, preferencia):
        self.mail = mail
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.preferencia = preferencia

class Bd():
    def conectar_base(self):
        #genera la conexion con sqlite
        con = sqlite3.connect('./bd_tp_final.db')
        return con
    
    def crear_tabla(self, con):
        #crea la tabla usuarios y categorias
        con = self.conectar_base()
        cursor = con.cursor()
        try:
            sql = "CREATE TABLE usuario(idusuario integer PRIMARY KEY, mail varchar(255) NOT NULL, nombre varchar(100) NOT NULL, apellido varchar(100) NOT NULL, sexo char(2), preferencia varchar(200))"
            print ("try crearTable")
            cursor.execute(sql)
            con.commit()
            sql= "CREATE TABLE categoria (id INTEGER PRIMARY KEY AUTOINCREMENT, descripcion_categoria VARCHAR (100) NOT NULL)"
            cursor.execute(sql)
            con.commit()

            lista_categorias=["Viajes", "Moda", "Deportes", "Autos", "Motos", "Recitales", "Gastronomia", "Cine", "Comidas"]
            for i in range(1,len(lista_categorias)):
                print ("Lista", lista_categorias[i])
                sql="INSERT INTO categoria (descripcion_categoria) VALUES ('" + lista_categorias[i] + "')"
                cursor.execute(sql) 
                con.commit()
            con.close
        except sqlite3.Error as er:
            print(f'Excepción: {er}')

class Abm():

    def funcion_grabar(self, tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
        con = Bd()
        con=con.conectar_base()
        validar=Validacion()
        validar.existe_tabla()

        datospersona=Persona(var_mail.get(), var_nombre.get(), var_apellido.get(), var_sexo.get(), var_preferencia.get())

        #Esta funcion graba el alta de un usuario
        global mi_id
        print ("ID___1 :", mi_id)
        resultado=Validacion()
        valor=resultado.funcion_validar_datos(datospersona.mail, datospersona.nombre, datospersona.apellido)
        print ("Valor es ", valor)
        if (valor != 1):
            mi_id += 1
            print ("ID___2 :", mi_id)
            try:
                tree.insert("", "end", text=str(mi_id), values=(datospersona.mail, datospersona.nombre, datospersona.apellido, datospersona.sexo, datospersona.preferencia))
                cursor = con.cursor()
                data = (str(mi_id), datospersona.mail, datospersona.nombre, datospersona.apellido, datospersona.sexo, datospersona.preferencia)
                sql = "INSERT INTO usuario(idusuario, mail, nombre, apellido, sexo, preferencia) VALUES(?,?, ?, ?, ?, ?)"
                print ("SQL INSERT *************************************", sql)
                cursor.execute(sql, data)
                con.commit()
                blanqueo=Pantalla()
                blanqueo.funcion_blanquear(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
                showinfo("Alta usuario", "Se registro un nuevo usuario")
            except:
                showwarning("Alta usuario", "Error al registrar usuario")
        con.close

    def carga_categoria(self,):
        con = Bd()
        con =con.conectar_base()
        cursor = con.cursor()
        sql = "SELECT * FROM categoria"
        cursor.execute(sql)
        con.commit()
        rows = cursor.fetchall()
        con.close
        return rows

    def dar_id_categoria(self, categoria):
        con = Bd()
        con =con.conectar_base()
        cursor = con.cursor()
        sql = "SELECT id FROM categoria where descripcion_categoria='" + categoria + "' "
        cursor.execute(sql)
        con.commit()
        rows = cursor.fetchall()
        con.close
        return rows

    def funcion_consultar(self, tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
        con = Bd()
        con=con.conectar_base()
        #Esta funcion permite hacer consulta de los registros en la base de datos
        #Vaciamos la grilla con los resultados
        for row in tree.get_children():
            tree.delete(row)
        cursor = con.cursor()
        #Sino se ingresan datos en la busqueda trae todo los datos
        if (var_nombre.get() == "" and var_mail.get() == "" and var_apellido.get() == "" and var_sexo.get() == "" and var_preferencia.get() == "" ):
            sql = "SELECT idusuario, mail, nombre, apellido, sexo, b.descripcion_categoria as preferencia FROM usuario INNER JOIN categoria as b ON preferencia = b.id  "
        else:
            sql = "SELECT idusuario, mail, nombre, apellido, sexo, b.descripcion_categoria as preferencia FROM usuario INNER JOIN categoria as b ON preferencia = b.id WHERE mail = '" + var_mail.get() + "' OR nombre = '" + var_nombre.get() + "' OR apellido = '" + var_apellido.get() + "' OR sexo = '" + var_sexo.get() + "' OR preferencia = '" + var_preferencia.get() + "' "
        cursor.execute(sql)
        con.commit()
        con.close
        rows = cursor.fetchall()
        #Mostramos los resultados
        if len(rows) == 0:
            showinfo("Busqueda", "No se encontro un resultado")

        for row in rows:
            tree.insert("", "end", text=str(row[0]), values=(row[1], row[2], row[3], row[4], row[5]))

    def funcion_eliminar(self, tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
        con = Bd()
        con=con.conectar_base()
        #elimina un usuario seleccionado, sino se selecciona un usuario muestra una alerta
        global mi_id
        print ("ID___3 :", mi_id)

        item = tree.focus()
    
        if item == "" :
            showwarning("Seleccion", "Debe seleccion un usuario")
        elif askyesno("Eliminacion de usuario", "Esta por eliminar este usuario, desea continuar?"):
            id_borrar=(tree.item(item)['text'][0])
            tree.delete(item)
            cursor = con.cursor()
            data = (id_borrar)
            sql = "DELETE from usuario where idusuario = ?;"
            try:
                cursor.execute(sql, data)
                con.commit()
                con.close
                showinfo("Eliminacion", "Se elimino el usuario")
                mi_id -= 1
                print ("ID___4 :", mi_id)
                pantalla=Pantalla()
                pantalla.funcion_blanquear(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
                self.funcion_consultar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
            except sqlite3.Error as er:
                print(f'Excepción: {er}')

    def funcion_modificar(self, tree, master, mail, nombre, apellido, sexo, preferencia, boton_eliminar, boton_grabar, boton_consultar, boton_modificacion):
        #modifica los datos del usuario
        global mi_id
        print ("ID___5 :", mi_id)

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
            cat=self.dar_id_categoria(tree.item(item)['values'][4])
            for row in cat:
                aux=row[0]
            
            preferencia.set(aux)
 
            boton=Pantalla()

            boton_grabar =BotonB(master, text="Alta",  bg="grey", command=None, state="disabled", width=10, drow=3, dcol=3, dsti="w")
            boton_eliminar =BotonB(master, text=" Baja ", bg="grey", command=None, state="disabled", width=10, drow=4, dcol=3, dsti="w")
            boton_cancelar= BotonB(master, text=" Cancelar ", bg="#DC324C", command=lambda:boton.funcion_cancelar(master, mail, nombre, apellido, sexo, preferencia), width=10, drow=5, dcol=4, dsti="w")
            boton_guardar_cambio= BotonB(master, text=" Guardar ", bg="#4EDC32", command=lambda:self.funcion_guardar_cambio(tree, master, mail, nombre, apellido, sexo, preferencia, boton_modificacion,boton_grabar, boton_consultar, boton_eliminar), width=10, drow=5, dcol=3, dsti="w")
    
    def funcion_guardar_cambio(self, tree, master, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia, boton_modificacion, boton_grabar, boton_consultar, boton_eliminar):
        con = Bd()
        con=con.conectar_base()
        #Guarda los cambios luego de una modificacion
        global mi_id
        print ("ID___6 :", mi_id)

        item = tree.focus()
        id=str((tree.item(item)['text'][0]))
        cursor = con.cursor()
        datospersona=Persona(var_mail.get(), var_nombre.get(), var_apellido.get(), var_sexo.get(), var_preferencia.get())
        print("que hay aca", datospersona.nombre)
        valor=Validacion()
        resultado=valor.funcion_validar_datos(datospersona.mail, datospersona.nombre, datospersona.apellido)
        if (resultado != 1):
            sql = "UPDATE usuario SET mail='" + datospersona.mail + "', nombre='" + datospersona.nombre + "', apellido= '" + datospersona.apellido + "', sexo= '" + datospersona.sexo + "', preferencia = '" + datospersona.preferencia + "'WHERE idusuario= '" + id + "';"
            print ("Sql: ",sql)
            cursor.execute(sql)
            con.commit()
            con.close
            pantalla=Pantalla()
            pantalla.funcion_blanquear(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)
            showinfo("Actualizacion", "Se han actualizado los datos")

            boton_cancelar= BotonB(master, text=" Cancelar ", bg="#DC324C", command=lambda:None, state="disabled",  width=10, drow=5, dcol=4, dsti="w", ocultar="true")
            boton_guardar_cambio= BotonB(master, text=" Guardar ", bg="#4EDC32", command=lambda:None, state="disabled",  width=10, drow=5, dcol=3, dsti="w", ocultar="true")  
            boton_grabar =BotonB(master, text="Alta",  bg="#326DDC", command=lambda: self.funcion_grabar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia), width=10, drow=3, dcol=3, dsti="w")
            boton_eliminar =BotonB(master, text=" Baja ", bg="#DC3232", command=lambda: self.funcion_eliminar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia), width=10, drow=4, dcol=3, dsti="w")
            boton_consultar =BotonB(master, text=" Consulta ", bg="grey", command=lambda: self.funcion_consultar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia), width=10, drow=3, dcol=4, dsti="w")
            boton_modificacion =BotonB(master, text=" Modificar", bg="grey", command=lambda: self.funcion_modificar(tree, master, var_mail,var_nombre,var_apellido, var_sexo, var_preferencia, boton_eliminar, boton_grabar,boton_consultar, boton_modificacion), width=10, drow=4, dcol=4, dsti="w")
            #self.funcion_consultar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)


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
        #if (self.funcion_validar_mail(mail) == 1):
        #    return 1
        if (self.funcion_validar_nombre(nombre) == 1):
                return 1
        
    def existe_tabla(self):
        con = Bd()
        con=con.conectar_base()
        #sino existe la tabla la crea, para evitar que genere un error por existencia de la tabla
        cursor = con.cursor()
        sql= "SELECT * FROM sqlite_master where type='table' and name='usuario'"
        cursor.execute(sql)
        con.commit()
        con.close
        rows = cursor.fetchall()
        if len(rows) == 0:
            try:
                print ("try crearTable")
                crear=Bd()
                crear.crear_tabla(con)
            except sqlite3.Error as er:
                print(f'Excepción: {er}')

class Pantalla():
    def funcion_blanquear(self, tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia):
        #Esta funcion borra los campos en los textbox para evitar ingresar datos repetidos o luego de la modificacion que sigan apareciendo
        var_mail.set("")
        var_nombre.set("")
        var_apellido.set("")
        var_sexo.set("")
        var_preferencia.set("")
        consulta=Abm()
        consulta.funcion_consultar(tree, var_mail, var_nombre, var_apellido, var_sexo, var_preferencia)

    def funcion_cancelar(self, master, mail, nombre, apellido, sexo, preferencia):
        #cancela la accion guardar al modificar
        self.funcion_blanquear(mail, nombre, apellido, sexo, preferencia)    
        obj=Abm()   
        boton_cancelar= BotonB(master, text=" Cancelar ", bg="#DC324C", command=lambda:None, state="disabled",  width=10, drow=5, dcol=4, dsti="w", ocultar="true")
        boton_guardar_cambio= BotonB(master, text=" Guardar ", bg="#4EDC32", command=lambda:None, state="disabled",  width=10, drow=5, dcol=3, dsti="w", ocultar="true")  
        boton_grabar =BotonB(master, text="Alta",  bg="#326DDC", command=lambda: obj.funcion_grabar(self.tree, self.var_mail, self.var_nombre, self.var_apellido, self.var_sexo, self.var_preferencia), width=10, drow=3, dcol=3, dsti="w")
        boton_eliminar =BotonB(master, text=" Baja ", bg="#DC3232", command=lambda: obj.funcion_eliminar(self.tree, self.var_mail, self.var_nombre, self.var_apellido, self.var_sexo, self.var_preferencia), width=10, drow=4, dcol=3, dsti="w")
        boton_consultar =BotonB(master, text=" Consulta ", bg="grey", command=lambda: obj.funcion_consultar(self.tree, self.var_mail, self.var_nombre, self.var_apellido, self.var_sexo, self.var_preferencia), width=10, drow=3, dcol=4, dsti="w")
        boton_modificacion =BotonB(master, text=" Modificar", bg="grey", command=lambda: obj.funcion_modificar(self.tree, self.master, self.var_mail, self.var_nombre, self.var_apellido, self.var_sexo, self.var_preferencia, boton_eliminar, boton_grabar,boton_consultar, boton_modificacion), width=10, drow=4, dcol=4, dsti="w")

