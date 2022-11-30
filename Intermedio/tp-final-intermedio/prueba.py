"""import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.init_ui()
          
    def init_ui(self):

       
        self.pack(fill=tk.BOTH, expand=1)

        f = ttk.Frame(padding = 8)

        ttk.Label(f, text = "Combobox").pack()
        self.cbCombo = ttk.Combobox(f,)
        self.cbCombo.bind("<<ComboboxSelected>>", self.on_selected)
        self.cbCombo.pack()
        
        f.pack(fill=tk.BOTH, expand=1)

    def on_open(self,):

        self.set_combos()
        self.on_set_combo()
        
    def set_combos(self):

        index = 0
        self.dict_cars = {}
        voices = []

        #here your recordset, I've add some items and even a supposed primary key.....1,2,3,4,5
        rs = [(1, 'Hyundai', 'Elantra', 'TEST123'),
              (2, 'Hyundai', 'I30', 'ABC123'),
              (6, 'Hyundai', 'Azera', 'ABC123'),
              (4, 'Hyundai', 'Sonata', 'ABC123'),
              (8, 'Hyundai', 'I30 Fastback N', 'ABC123')]

        #here we coupling self.dict_cars with the combo index...
        for i in rs:
            self.dict_cars[index] = i[0]
            index += 1
            record = "{0} {1}".format(i[1], i[2])
            voices.append(record)

        self.cbCombo["values"] = voices        
        

    def on_selected(self, evt=None):
        #when you select an item on the combo it get the relative pk record from the dict
        index = self.cbCombo.current()
        pk = self.dict_cars[index]
        msg =  ("You have selected index {0} pk {1}".format(index, pk))

        messagebox.showinfo(self.master.title(),msg, parent=self)
        
    def on_set_combo(self):
        #it'use to select, on open a specific record, in that case the 5
        try:
            key = next(key
                       for key, value
                       in self.dict_cars.items()
                       if value == 5)
            self.cbCombo.current(key)
        except:
            pass
        
        
    def on_close(self):
        self.parent.on_exit()

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.protocol("WM_DELETE_WINDOW", self.on_exit)
            
        self.set_title()
        self.set_style()
       
        frame = Main(self,)
        frame.on_open()
        frame.pack(fill=tk.BOTH, expand=1)

    def set_style(self):
        self.style = ttk.Style()
        #('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
        self.style.theme_use("clam")
        

    def set_title(self):
        s = "{0}".format('Simple App')
        self.title(s)
        
    def on_exit(self):
        if messagebox.askokcancel("Simple App", "Do you want to quit?", parent=self):
            self.destroy()               
    
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

import tkinter as tk
from tkinter import ttk
my_w = tk.Tk()
my_w.geometry("400x150")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title
my_dict={'A':5,'B':4,'C':3,'D':3,'E':1,'F':0} 
months=list(my_dict.keys()) # All keys are taken as options 
font1=('Times',18,'normal')
def my_upd(*args):
    str1.set(sel.get()) #  Key name A B C D is displayed 
    str2.set(my_dict[sel.get()]) # value of the key is displayed

sel=tk.StringVar() # string variable for the Combobox
cb1=ttk.Combobox(my_w,values=months,width=7,
    textvariable=sel,font=font1)
cb1.grid(row=1,column=1,padx=10, pady=20)    
str1=tk.StringVar("B") # for entry1
str2=tk.StringVar() # for entry2

l1=tk.Entry(my_w,font=font1,width=5,textvariable=str1)
l1.grid(row=1,column=2,padx=5)

l2=tk.Entry(my_w,font=font1,width=5,textvariable=str2)
l2.grid(row=1,column=3,padx=5)

sel.trace('w',my_upd)
my_w.mainloop()  # Keep the window open