from tkinter import *
from tkinter import ttk
 
root = Tk()

"""*************************************
* PASO 1
*************************************"""
lab_base=Label(root, text="Seleccionar base -->", bg="blue", fg="thistle1")
lab_base.grid(row=1, column=2)

def valor_combobox():
    global valor_com, com1
    valor_com=StringVar()
    valor_com.trace('w', la_base_es)
    com1=ttk.Combobox(root, textvariable=valor_com)
    com1['values']=('sqlite3', 'mysql')
    com1.grid(row=1, column=3)

def la_base_es( *args): 
    global valor_com, com1    
    try:
        print(com1.get())

    except ValueError:
        print("error")  

valor_combobox()
root.mainloop()