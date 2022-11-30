from tkinter import ttk
from tkinter import *
import random
from tkinter.colorchooser import askcolor
from turtle import width

aplicacion = Tk()

aplicacion.title("Tarea POO")
subtitulo = Label(aplicacion, text="Ingrese los Datos", width=80)
subtitulo.grid(row=0, columnspan=6)
subtitulo.config(bg="purple")

info= {}

n = 0

el_titulo = Label(aplicacion, text="Título")
el_titulo.grid(row = 1, column = 0, sticky=W)
la_ruta = Label(aplicacion, text="Ruta")
la_ruta.grid(row=2, column = 0, sticky=W)
la_descripcion = Label(aplicacion, text="Descripción")
la_descripcion.grid(row=3, column = 0, sticky=W)

entry_titulo = Entry(aplicacion)
entry_titulo.grid(row = 1, column = 3, sticky=E)
entry_ruta = Entry(aplicacion)
entry_ruta.grid(row = 2, column = 3, sticky=E)
entry_descripcion = Entry (aplicacion)
entry_descripcion.grid(row = 3, column = 3, sticky=E)


def funcion_alta():
    titulo = entry_titulo.get()
    ruta = entry_ruta.get()
    descripcion = entry_descripcion.get()
    global n
    n+=1
    info['Registro N° ' + str(n)]= [titulo, ruta, descripcion]
    print("Nueva Alta de Datos ") 
    print(info)

def funcion_sorpresa():
    #colores = ["#FF0000", "#FFFF00", "#00FF00", "#00FFFF", "#FF00FF"]
    #colores_random = random.choice(colores)                                        #variante para pintar la APP con colores random
    #aplicacion.config(background=colores_random)
    resultado = askcolor(color="#FF0000", title="Elija color de la APP")
    aplicacion.config(background=resultado[1])

boton_a = Button(aplicacion, text="Alta", command=funcion_alta)
boton_a.grid(row = 4, column = 2)

boton_s = Button(aplicacion, text="Sorpresa", command=funcion_sorpresa)
boton_s.grid(row = 4, column = 3)

aplicacion.mainloop()