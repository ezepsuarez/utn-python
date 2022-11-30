import sqlite3

def crear_base():
    con = sqlite3.connect('desafio_unidad_6.db')
    return con

def crear_tabla(con):

    cursor = con.cursor()
    sql = "CREATE TABLE personas(id integer PRIMARY KEY, titulo text, ruta text, descripcion text)"
    cursor.execute(sql)
    con.commit()

con = crear_base()
crear_tabla(con)
