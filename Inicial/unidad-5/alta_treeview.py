from tkinter import *
from tkinter import ttk

ID = 0
# Defino las funciones para agregar y borrar autores
def fagregar():
    global ID
    ID += 1
    tree.insert("", "end", text=str(ID), values=(e_text1.get(),
         e_text2.get(), e_text3.get()))


def fborrar():
    global ID
    item = tree.focus()
    tree.delete(item)
    ID -= 1


# Defino la ventana principal de la aplicación
root = Tk()

# Defino las variables que voy a usar
Nombre1 = StringVar()
Nombre2 = StringVar()
Apellido = StringVar()


# Fijo el tamaño de la ventana y el título
root.resizable(width=False, height=False)
root.title('Base de datos de Autores')

# Creo las etiquetas y los botones
l_Nombre1 = ttk.Label(root, text="1° Nombre")
l_Nombre2 = ttk.Label(root, text="2° Nombre")
l_Apellido = ttk.Label(root, text="Apellido")

e_text1 = ttk.Entry(root, textvariable=Nombre1, width=15)
e_text2 = ttk.Entry(root, textvariable=Nombre2, width=15)
e_text3 = ttk.Entry(root, textvariable=Apellido, width=15)

b_agregar = ttk.Button(root, text='Agregar', command=fagregar)
b_borrar = ttk.Button(root, text='Borrar', command=fborrar)
b_salir = ttk.Button(root, text='Salir', command=root.quit)

tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2", "col3")
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("col1", width=80, minwidth=80)
tree.column("col2", width=80, minwidth=80)
tree.column("col3", width=100, minwidth=100)

# Posiciono los controles
l_Nombre1.grid(column=0, row=0)
l_Nombre2.grid(column=0, row=1)
l_Apellido.grid(column=0, row=2)
e_text1.grid(column=1, row=0)
e_text2.grid(column=1, row=1)
e_text3.grid(column=1, row=2)
tree.grid(column=0, row=3, columnspan=4)
b_agregar.grid(column=3, row=0)
b_borrar.grid(column=3, row=1)
b_salir.grid(column=3, row=5)



mainloop()