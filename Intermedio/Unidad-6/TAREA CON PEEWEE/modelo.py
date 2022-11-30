import sqlite3
from peewee import *
from tkinter import ttk
from tkinter import messagebox
import re

db = SqliteDatabase("bd_peewee.db")


class BaseModel(Model):
    class Meta:
        database = db


class Alumnos(BaseModel):
    nombre = CharField(unique=True)
    apellido = CharField()
    materia = CharField()
    nota = CharField()


db.connect()
db.create_tables([Alumnos])


class BasesDatos:
    def __init__(
        self,
    ):
        pass

    def alta(self, nombre, apellido, materia, nota, tree):
        control = "^[A-Za-záéíóú]*$"
        persona = Alumnos()
        persona.nombre = nombre.get()
        persona.apellido = apellido.get()
        persona.materia = materia.get()
        persona.nota = nota.get()
        if re.match(control, persona.nombre):
            persona.save()
            messagebox.showinfo("Alta", "Alta satisfactoria")
        else:
            print("error en campo del nombre")
            messagebox.showinfo("Alta", "Error en tipeo del nombre")
        self.actualizar_treeview(tree)

    def actualizar_treeview(self, mitreeview):
        grabados = mitreeview.get_children()
        for elementos in grabados:
            mitreeview.delete(elementos)
        for fila in Alumnos.select():
            mitreeview.insert(
                "",
                0,
                text=fila.id,
                values=(fila.nombre, fila.apellido, fila.materia, fila.nota),
            )

    def borrar(self, tree):
        valor = tree.focus()
        item = tree.item(valor)
        baja = Alumnos.get(Alumnos.id == item["text"])
        baja.delete_instance()
        self.actualizar_treeview(tree)
        messagebox.showinfo("Borrar", "Elemento eliminado")

    def modificar_no(self, nombre, tree):
        valor = tree.focus()
        item = tree.item(valor)
        actualizar = Alumnos.update(nombre=nombre.get()).where(
            Alumnos.id == item["text"]
        )
        actualizar.execute()
        self.actualizar_treeview(tree)
        messagebox.showinfo("Actualizar", "Nombre actualizado exitosamente !!")

    def modificar_ap(self, apellido, tree):
        valor = tree.focus()
        item = tree.item(valor)
        actualizar = Alumnos.update(apellido=apellido.get()).where(
            Alumnos.id == item["text"]
        )
        actualizar.execute()
        self.actualizar_treeview(tree)
        messagebox.showinfo("Actualizar", "Apellido actualizado exitosamente !!")

    def modificar_ma(self, materia, tree):
        valor = tree.focus()
        item = tree.item(valor)
        actualizar = Alumnos.update(materia=materia.get()).where(
            Alumnos.id == item["text"]
        )
        actualizar.execute()
        self.actualizar_treeview(tree)
        messagebox.showinfo("Actualizar", "Materia actualizada exitosamente !!")

    def modificar_nt(self, nota, tree):
        valor = tree.focus()
        item = tree.item(valor)
        actualizar = Alumnos.update(nota=nota.get()).where(Alumnos.id == item["text"])
        actualizar.execute()
        self.actualizar_treeview(tree)
        messagebox.showinfo("Actualizar", "Nota actualizada exitosamente !!")

    def consultar(self, tree):
        self.actualizar_treeview(tree)
