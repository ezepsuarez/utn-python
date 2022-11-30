import sqlite3

def crear_conexion():
    con = sqlite3.connect('personas.db')
    return con


def crear_tabla(con):
    cursor = con.cursor()
    sql = "CREATE TABLE persona(id integer PRIMARY KEY AUTOINCREMENT, nombre VARCHAR, apellido VARCHAR, dni VARCHAR, sexo VARCHAR, fecha_nacimiento DATE, nacionalidad VARCHAR, puesto_laboral VARCHAR, sueldo FLOAT, fecha_ingreso DATE)"
    try:
        cursor.execute(sql)
        con.commit()
    except sqlite3.Error as er:
        print(f'Excepción: {er}')


def insert_sqlite(con, per):
    cursor = con.cursor()
    data = (per.nombre, per.apellido, per.dni, per.sexo, per.fecha_nacimiento, per.nacionalidad, per.puesto_laboral, per.sueldo, per.fecha_ingreso)
    sql = "INSERT INTO persona(nombre, apellido, dni, sexo, fecha_nacimiento, nacionalidad, puesto_laboral, sueldo, fecha_ingreso) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
    try:
        cursor.execute(sql, data)
        con.commit()
    except sqlite3.Error as er:
        print(f'Excepción: {er}')


def update_sqlite(con, per):
    cursor = con.cursor()
    data = (per.nombre, per.apellido, per.puesto_laboral, per.sueldo, per.id)
    sql = "UPDATE persona SET nombre = ?, apellido = ?, puesto_laboral = ?, sueldo = ? WHERE id = ?"
    try:
        cursor.execute(sql, data)
        con.commit()
    except sqlite3.Error as er:
        print(f'Excepción: {er}')


def delete_sqlite(con, per):
    cursor = con.cursor()
    data = (per.id,)
    sql = "DELETE FROM persona WHERE id = ?"
    try:
        cursor.execute(sql, data)
        con.commit()
    except sqlite3.Error as er:
        print(f'Excepción: {er}')


def select_sqlite(con):
    cursor = con.cursor()
    sql = "SELECT * FROM persona"
    try:
        result = cursor.execute(sql)
        con.commit()
    except sqlite3.Error as er:
        print(f'Excepción: {er}')
    return result