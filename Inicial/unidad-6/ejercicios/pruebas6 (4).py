from tkinter import * 
from tkinter import ttk
from tkinter.messagebox import *

mi_id=0

master = Tk()

var_nombre= StringVar()
var_apellido= StringVar()

nombre = Label(master, text="Nombre :")
nombre.grid(row=1, column=1, sticky=W)

apellido = Label(master, text="Apellido :")
apellido.grid(row=2, column=1, sticky=W)

nombre = Entry(master, textvariable=var_nombre, width=30)
nombre.grid (row=1, column=2,sticky=W)

apellido = Entry(master, textvariable=var_apellido, width=30)
apellido.grid (row=2, column=2,sticky=W)

tree = ttk.Treeview(master)
tree['columns'] = ("col1", "col2", "col3")
tree.column("#0", width=20, minwidth=20, anchor=W)
tree.column("col1", width=80, minwidth=80, anchor=W)
tree.column("col2", width=80, minwidth=80, anchor=W)
tree.column("col3", width=100, minwidth=100, anchor=W)
tree.grid(column=0, row=4, columnspan=4)


def funcion_grabar():
    global mi_id
    mi_id += 1
    tree.insert("", "end", text=str(mi_id), values=(var_nombre.get(), var_apellido.get()))
    print(f"Nombre: {var_nombre.get()}  - Apellido {var_apellido.get()}")

def funcion_sorpresa():
    print("sorpresa")
    if askyesno('Cambio de color','Desea cambiar el color?'):
        master.configure(bg="blue")
        showinfo('Si', 'Cambio realizado')
    else:
        showinfo('No', 'Esta a punto de salir')

boton_grabar =Button(master, text="Alta", command=funcion_grabar)
boton_grabar.grid(row=3, column=2, sticky=W)

boton_eliminar= Button(master, text="Sorpresa", command=funcion_sorpresa)
boton_eliminar.grid(row=3, column=3,sticky=W)

master.mainloop()