import sqlite3
from tkinter import messagebox

import re
import regex


# Creo base y tabla


class Crud:
    def __init__(
        self,
    ):
        self.ob_nom = regex.Regex()
        try:
            conexion = self.conexion()
            cursor = conexion.cursor()
            conexion.execute(
                """CREATE TABLE usuarios (id integer PRIMARY KEY AUTOINCREMENT, 
                Nombre VARCHARD(50) NOT NULL, 
                Apellido VARCHARD(50), Edad integer, DNI integer)"""
            )
            print("Se creo la tabla Usuarios")
            cursor.execute(conexion)
            conexion.commit()
        except:
            print("error")

    def conexion(
        self,
    ):
        conexion = sqlite3.connect("clientes.db")
        return conexion

    # Agrego registros *
    def alta(self, nombre, apellido, edad, dni, tree):
        """cadena = nombre
        patron = "^[A-Za-záéíóú]*$"
        if re.match(patron, cadena):
            print(nombre, apellido, edad, dni)"""
        
        nombre_validado=self.ob_nom.regex_nom(nombre.get())
        if nombre_validado:
            print("cargar registyro")
            return "parámetro correcto"
        else:
            return "El nombre debe ser ........."
        
        """
        con = self.conexion()
        cursor = con.cursor()
        data = (nombre, apellido, edad, dni)
        sql = "INSERT INTO usuarios(nombre, apellido, edad, dni) VALUES(?, ?, ?,?)"
        cursor.execute(sql, data)
        con.commit()
        print("Guardado Correctamene")
        self.actualizar_treeview(tree)""" 
        """messagebox.showwarning(
            message="El registro se agrego correctamente", title="Información"
        )
        else:
            messagebox.showwarning(
                message="No se registro el alta del cliente", title="Información"
            )
            print("Error en campo Nombre")"""

    # Consulta
    def consulta_base(self, tree):
        con = self.conexion()
        cursor = con.cursor()
        cursor = con.execute("select id,nombre, apellido, edad, dni from usuarios")
        for fila in cursor:
            messagebox.showwarning(message=fila, title="Información")
            print(fila)
            messagebox.showwarning(message=fila, title="Información")
        con.close

    # Buscar una fila  *
    def buscar_registro(self, brdni, tree):
        con = self.conexion()
        cursor = con.cursor()
        dni = brdni
        print(dni)
        cursor = con.execute("SELECT * FROM usuarios where dni=?", (dni,))
        dni = tree.focus()
        fila = cursor.fetchall()
        if fila != None:
            messagebox.showinfo(message=fila, title="Registro")
            print(fila)
        else:
            messagebox.showwarning(
                message="No existe Cliente con el DNI ingresado.", title="Información"
            )
            print("No existe Cliente con el Id ingresado.")
        con.close()

    # Modificar registros *
    def modificar_registro(self, nombre, apellido, edad, dni, tree):
        try:
            valor = tree.selection()
            print(valor)
            item = tree.item(valor)
            print(item)
            print(item["text"])
            mi_id = item["text"]
            datos = (nombre, apellido, edad, dni, mi_id)
            sentencia = """UPDATE usuarios SET nombre = ?, apellido = ?, edad = ?, dni = ? WHERE id = ?;"""
            con = self.conexion()
            cursor = con.cursor()
            cursor.execute(sentencia, datos)
            con.commit()
            self.actualizar_treeview(tree)
            print("Registo Modificaco con exito")
            messagebox.showinfo(
                message="Registo Modificaco con exito", title="Información"
            )
        except sqlite3.sqlite3.OperationalError as error:
            messagebox.showwarning(
                message="No se encontro registro para modificar", title="Información"
            )
            print("Error al actualizar: ", error)

    # Eliminar registro *
    def eliminar(self, tree):
        try:
            valor = tree.selection()
            print(valor)
            item = tree.item(valor)
            print(item["text"])
            mi_id = item["text"]
            con = self.conexion()
            cursor = con.cursor()
            dato = (mi_id,)
            eliminar = "DELETE FROM usuarios WHERE id=?;"
            cursor.execute(eliminar, dato)
            con.commit()
            tree.delete(valor)
            messagebox.showwarning(
                message="El registro se elimino correctamente", title="Información"
            )
            if not mi_id:
                print("No se ingreso registro")
                exit()
        except sqlite3.OperationalError as error:
            messagebox.showwarning(
                message="No se encontro registro para eliminar", title="Información"
            )
            print("Error al eliminar: ", error)
        self.actualizar_treeview(tree)

    # Actualizar treeview
    def actualizar_treeview(self, mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)

        sql = "SELECT * FROM usuarios ORDER BY id ASC"
        con = self.conexion()
        cursor = con.cursor()
        datos = cursor.execute(sql)

        resultado = datos.fetchall()
        for fila in resultado:
            print(fila)
            mitreview.insert(
                "", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4])
            )
