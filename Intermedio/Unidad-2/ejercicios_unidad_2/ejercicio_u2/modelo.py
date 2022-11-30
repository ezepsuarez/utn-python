from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno

import sqlite3
import re


# Se verifica si la base de datos existe. En caso negativo se crea
# la base de datos.
def base():
    conectar = sqlite3.connect("biblioteca.db")
    return conectar


# Se verifica si la tabla existe. En caso negativo se crea la tabla.
def tabla(conectar):
    cursor = conectar.cursor()
    sql = "CREATE TABLE IF NOT EXISTS libros(id INTEGER PRIMARY KEY \
        AUTOINCREMENT, genero VARCHAR, apellido VARCHAR, nombres VARCHAR, \
        titulo VARCHAR, cantidad INTEGER);"
    cursor.execute(sql)
    conectar.commit()


# Se crea función para el alta de registros.
def alta(conectar, tree, variables):

    data = []

    for x in range(len(variables)):
        data.append(variables[x].get())

    data = tuple(data)

    patron = "^[\sa-zA-Z]*$"

    if re.match(patron, variables[1].get()):
        cursor = conectar.cursor()
        sql = "INSERT INTO libros(genero, apellido, nombres, titulo, \
                cantidad) VALUES(?, ?, ?, ?, ?);"
        cursor.execute(sql, data)
        conectar.commit()
        limpiar(variables)
        actualizar_vista(conectar, tree)
        showinfo("Mensaje", "Registro ingresado.")
    else:
        showerror(
            "Error de integridad",
            "El campo 'Apellido' sólo acepta caracteres alfabéticos \
y espacios en blanco.",
        )


# Se crea función para eliminar registros.
def baja(conectar, tree, variables):
    if askyesno("Sistema", "¿Desea eliminar el registro seleccionado?"):
        seleccion = tree.selection()
        for registro in seleccion:
            id_registro = tree.item(registro)["text"]
            cursor = conectar.cursor()
            data = (id_registro,)
            sql = "DELETE FROM libros WHERE id = ?;"
            cursor.execute(sql, data)
            conectar.commit()
            tree.delete(registro)
        showinfo("Mensaje", "Registro eliminado.")
    else:
        showinfo("Mensaje", "Operación cancelada.")
    limpiar(variables)


# Se crea función para modificar registros.
def modificar(conectar, tree, variables):
    registro = tree.selection()
    id_registro = tree.item(registro)["text"]
    cursor = conectar.cursor()

    data = []

    for x in range(len(variables)):
        data.append(variables[x].get())
    data.append(id_registro)

    data = tuple(data)

    sql = "UPDATE libros SET genero=?, apellido=?, nombres=?, titulo=?, \
        cantidad=? WHERE id=?"
    cursor.execute(sql, data)
    conectar.commit()
    limpiar(variables)
    actualizar_vista(conectar, tree)
    showinfo("Mensaje", "Registro modificado.")


# Se crea función para consultar por autor o la tabla completa.
def consultar(conectar, tree, apellido):
    if apellido == "":
        actualizar_vista(conectar, tree)
    else:
        data = (apellido,)
        sql = "SELECT * FROM libros WHERE apellido=?"
        cursor = conectar.cursor()
        datos = cursor.execute(sql, data)
        registros = tree.get_children()
        tree.delete(*registros)
        seleccion = datos.fetchall()
        for registro in seleccion:
            tree.insert(
                "",
                0,
                text=registro[0],
                values=(
                    registro[1],
                    registro[2],
                    registro[3],
                    registro[4],
                    registro[5],
                ),
            )


# Se crea función para limpiar los campos de entrada.
def limpiar(variables):
    for variable in variables:
        variable.set("")


# Se crea función para actualizar la vista del visor de registros.
def actualizar_vista(conectar, tree):
    sql = "SELECT * FROM libros ORDER BY id DESC"
    cursor = conectar.cursor()
    datos = cursor.execute(sql)
    registros = tree.get_children()
    tree.delete(*registros)
    seleccion = datos.fetchall()
    for registro in seleccion:
        tree.insert(
            "",
            0,
            text=registro[0],
            values=(
                registro[1],
                registro[2],
                registro[3],
                registro[4],
                registro[5],
            ),
        )


# Se crea función para seleccionar registros con doble click.
def seleccion(tree, entradas, variables):
    registro = tree.selection()
    valores = tree.item(registro)["values"]
    for x in range(len(entradas)):
        entradas[x] = variables[x].set(valores[x])


# Se crea función para confirmar salida del sistema.
def salir(root):
    if askyesno("Sistema", "¿Desea salir del sistema?"):
        showinfo("Mensaje", "Ha salido del sistema")
        root.quit()
    else:
        showinfo("Mensaje", "Operacón cancelada")
