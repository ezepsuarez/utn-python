import sqlite3
from sqlite3 import Error
# ############# CREAR BASE DE DATOS


def crear_base():

    con = sqlite3.connect('desafio_unidad_6.db')
    return con

crear_base()