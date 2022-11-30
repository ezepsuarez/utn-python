import re
import tkinter
from tkinter import messagebox
from connection import delete_sqlite, insert_sqlite, select_sqlite, update_sqlite


class Persona():
    def __init__(self, nombre, apellido, dni, sexo, sueldo, nacionalidad, fecha_nacimiento, fecha_ingreso, puesto_laboral, id=None):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.sexo = sexo
        self.sueldo = sueldo
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso
        self.puesto_laboral = puesto_laboral
        self.id = id


def reiniciar_agregar(var_nombre_agregar, var_apellido_agregar, var_DNI_agregar, var_sueldo_agregar, var_nacionalidad_agregar, var_puesto_agregar):
    var_nombre_agregar.set("")
    var_apellido_agregar.set("")
    var_DNI_agregar.set("")
    var_sueldo_agregar.set(0)
    var_nacionalidad_agregar.set("")
    var_puesto_agregar.set("")


def reiniciar_modificar(var_nombre_modificar, var_apellido_modificar, var_sueldo_modificar, var_puesto_modificar):
    var_nombre_modificar.set("")
    var_apellido_modificar.set("")
    var_sueldo_modificar.set(0)
    var_puesto_modificar.set("")


def validar_entry(fecha_nacimiento):
    validate = False
    if re.match('^[\d]{4}-[\d]{2}-[\d]{2}$', fecha_nacimiento):
        validate = True
    return validate


def agregar(
    var_nombre_agregar, 
    var_apellido_agregar, 
    var_DNI_agregar, 
    var_sexo_agregar, 
    var_sueldo_agregar, 
    var_nacionalidad_agregar, 
    var_fecha_nacimiento_agregar, 
    var_fecha_ingreso_agregar, 
    var_puesto_agregar, 
    tree, 
    con):
    persona = Persona(
        var_nombre_agregar.get(), 
        var_apellido_agregar.get(), 
        var_DNI_agregar.get(), 
        var_sexo_agregar.get()[0], 
        var_sueldo_agregar.get(), 
        var_nacionalidad_agregar.get(), 
        var_fecha_nacimiento_agregar.get(), 
        var_fecha_ingreso_agregar.get(), 
        var_puesto_agregar.get())
    res = validar_entry(persona.fecha_nacimiento)
    if res:
        insert_sqlite(con, persona)
        listar(tree, con)
        messagebox.showinfo("Persona agregada", "La persona fue agregada correctamente")
        reiniciar_agregar(var_nombre_agregar, var_apellido_agregar, var_DNI_agregar, var_sueldo_agregar, var_nacionalidad_agregar, var_puesto_agregar)
    else:
        messagebox.showerror("Error de validación", "El campo no coincide con el formato especificado")


def modificar(
    var_id_modificar, 
    var_sueldo_modificar, 
    var_nombre_modificar, 
    var_apellido_modificar, 
    var_puesto_modificar, 
    tree, 
    con):
    try:
        item_viejo = tree.item(var_id_modificar.get())['values']
        try:
            sueldo = var_sueldo_modificar.get()
        except:
            sueldo = item_viejo[8]
        persona = Persona(
            var_nombre_modificar.get() if var_nombre_modificar.get()!='' else item_viejo[1], 
            var_apellido_modificar.get() if var_apellido_modificar.get()!='' else item_viejo[2], 
            item_viejo[3], 
            item_viejo[4], 
            sueldo, 
            item_viejo[6], 
            item_viejo[5], 
            item_viejo[9], 
            var_puesto_modificar.get() if var_puesto_modificar.get()!='' else item_viejo[7],
            var_id_modificar.get())
        update_sqlite(con, persona)
        listar(tree, con)
        messagebox.showinfo("Persona modificar", "La persona fue modificada correctamente")
        reiniciar_modificar(var_nombre_modificar, var_apellido_modificar, var_sueldo_modificar, var_puesto_modificar)
    except tkinter.TclError as er:
        print(f'Excepción: {er}')
        messagebox.showerror("No se pudo modificar", "Debe ingresar un id correcto")
    


def eliminar(var_id_eliminar, tree, con):
    item_viejo = tree.item(var_id_eliminar.get())['values']
    persona = Persona(
        item_viejo[1], 
        item_viejo[2], 
        item_viejo[3], 
        item_viejo[4], 
        item_viejo[8], 
        item_viejo[6], 
        item_viejo[5], 
        item_viejo[9], 
        item_viejo[7],
        var_id_eliminar.get())
    pregunta = messagebox.askyesno(message=f"¿Desea eliminar la persona {persona.id}?", title="Confirmación eliminar")
    if pregunta:
        delete_sqlite(con, persona)
        listar(tree, con)
        messagebox.showinfo("Persona eliminada", "La persona fue eliminada correctamente")
        

def listar(tree, con):
    for i in tree.get_children():
        tree.delete(i)
    result = select_sqlite(con)
    for dt in result: 
        tree.insert("",'end',iid=dt[0],values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],dt[9]))