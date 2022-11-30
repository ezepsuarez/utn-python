from tkinter import *
import tkinter as tk

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import time
from PIL import Image, ImageTk
import random
from pygame import mixer

from tkinter import *

try:
    # Tkinter for Python 2.xx
    import Tkinter as tk
except ImportError:
    # Tkinter for Python 3.xx
    import tkinter as tk
APP_TITLE = "Pokemon Game"
APP_XPOS = 100
APP_YPOS = 100
APP_WIDTH = 300
APP_HEIGHT = 200
IMAGE_PATH = "images/"
mixer.init()

class CreateCanvasObject(object):
    def __init__(self, canvas, image_name, xpos, ypos):
        self.canvas = canvas
        self.image_name = image_name
        self.xpos, self.ypos = xpos, ypos

        #image = Image.open("C:\\Users\\happy\\Desktop\\test.jpg")
        #photo = ImageTk.PhotoImage(image)

        self.tk_image = ImageTk.PhotoImage(
            file="{}{}".format(IMAGE_PATH, image_name))
        self.image_obj= canvas.create_image(
            xpos, ypos, image=self.tk_image)



#        self.tk_image = tk.PhotoImage(
#            file="{}{}".format(IMAGE_PATH, image_name))
#        self.image_obj= canvas.create_image(
#            xpos, ypos, image=self.tk_image)
        canvas.tag_bind(self.image_obj, '<Button1-Motion>', self.move)
        canvas.tag_bind(self.image_obj, '<ButtonRelease-1>', self.release)
        self.move_flag = False
        #self.text_id = self.canvas.create_text(950,50, font='Times 24',text="                                                                 ")
    def move(self, event):
        #self.image_obj[0]:
        #print(self.image_1.x)
        if self.move_flag:
            new_xpos, new_ypos = event.x, event.y
            self.canvas.move(self.image_obj,
                new_xpos-self.mouse_xpos ,new_ypos-self.mouse_ypos)
            self.mouse_xpos = new_xpos
            self.mouse_ypos = new_ypos
        else:
            self.move_flag = True
            self.canvas.tag_raise(self.image_obj)
            self.mouse_xpos = event.x
            self.mouse_ypos = event.y
    def release(self, event):
        self.move_flag = False
class Application(tk.Frame):
    def __init__(self, master):
        #print(self)
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Frame.__init__(self, master)
        self.canvas = tk.Canvas(self, width=400, height=400, bg='#AFFAAF',
            highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        pokemons = ["Charizard", "Charmeleon", 'Charmander', 'Blastoise', 'Wartortle','Squirtle','Venusaur','Ivysaur','Bulbsaur']
        random.shuffle(pokemons)
        for i in range(0,9):
            self.image_1 = CreateCanvasObject(self.canvas,pokemons[i]+'.png', 100*i+350, 500)
            #self.image_2 =CreateCanvasObject(self.canvas, "Charmeleon.png", 200, 500)
            #self.image_3 = CreateCanvasObject(self.canvas, "Charmander.png", 300, 500)
            #self.image_4 =CreateCanvasObject(self.canvas, "Blastoise.png", 400, 500)
            #self.image_5 = CreateCanvasObject(self.canvas, "Wartortle.png", 500, 500)
            #self.image_6 =CreateCanvasObject(self.canvas, "Squirtle.png", 600, 500)
            #self.image_7 =CreateCanvasObject(self.canvas, "Venusaur.png", 700, 500)
            #self.image_8 = CreateCanvasObject(self.canvas, "Ivysaur.png", 800, 500)
            #self.image_9 =CreateCanvasObject(self.canvas, "Bulbsaur.png", 900, 500)
        self.canvas.create_rectangle(350, 50, 600, 300) # fill='white')
        self.canvas.create_rectangle(650, 50, 900, 300) #, fill='white')
        self.canvas.create_rectangle(950, 50, 1200, 300) #, fill='white')
        self.canvas.create_rectangle(320, 550, 1250, 450)
        self.text_id1 = self.canvas.create_text(500,750, font='Times 24',text="")
        self.text_id = self.canvas.create_text(650,750, font='Times 24',text="")
        self.text_id2 = self.canvas.create_text(800,750, font='Times 24',text="")
        self.text_id3 = self.canvas.create_text(1000,750, font='Times 24',text="")
        self.text_id4 = self.canvas.create_text(800,400, font='Times 24',text="Drag the pokemons in their right evolution place. When you finished, press [Calculate] ")
        set1={pokemons.index('Charizard')+1,pokemons.index('Charmeleon')+1,pokemons.index('Charmander')+1}
        set2={pokemons.index('Blastoise')+1,pokemons.index('Wartortle')+1,pokemons.index('Squirtle')+1}
        set3={pokemons.index('Venusaur')+1,pokemons.index('Ivysaur')+1,pokemons.index('Bulbsaur')+1}
        labelframe=LabelFrame(self.canvas,text="",width=1500,height=800,highlightcolor="yellow",highlightbackground="red",highlightthickness=10)  
        labelframe.grid(padx = 0, pady = 0)
        def destroy():
            labelframe.destroy()
        self.mybutton2 = tk.Button(labelframe, text='Play', width=50, height=5, command=destroy)
        self.mybutton2.place(x=0,y=0)
    


        pokemon_names = []
        mixer.music.load('Muisc (1).wav')
        mixer.music.play(-1)


        def button_event():
            Frame1=[]
            Frame2=[]
            Frame3=[]
            for i in range(1,10): #print out every image object's coordinates
                #print(i, self.canvas.coords(i))
                if self.canvas.coords(i)[0] >= 350 and self.canvas.coords(i)[0] <= 600 and self.canvas.coords(i)[1] >= 50 and self.canvas.coords(i)[1] <= 300:
                    Frame1.append(i)
                if self.canvas.coords(i)[0] >= 650 and self.canvas.coords(i)[0] <= 900 and self.canvas.coords(i)[1] >= 50 and self.canvas.coords(i)[1] <= 300:
                    Frame2.append(i)
                if self.canvas.coords(i)[0] >= 950 and self.canvas.coords(i)[0] <= 1200 and self.canvas.coords(i)[1] >= 50 and self.canvas.coords(i)[1] <= 300:
                    Frame3.append(i)
            TP=0
            FP=0
            Level = 1



          
            

            for i in Frame1:
                for j in Frame1:
                    if i<j:
                        if (i in set1 and j in set1) or (i in set2 and j in set2) or (i in set3 and j in set3):
                            TP+=1
                        else:
                            FP+=1

            Undiscovered=0
            for i in set1:
                for j in set1:
                    if i<j:
                        Undiscovered+=1
                        if (i in Frame1 and j in Frame1) or (i in Frame2 and j in Frame2) or (i in Frame3 and j in Frame3):
                            Undiscovered-=1

            for i in Frame2:
                for j in Frame2:
                    if i<j:
                        if (i in set1 and j in set1) or (i in set2 and j in set2) or (i in set3 and j in set3):
                            TP+=1
                        else:
                            FP+=1

            #Undiscovered=0
            for i in set2:
                for j in set2:
                    if i<j:
                        Undiscovered+=1
                        if (i in Frame1 and j in Frame1) or (i in Frame2 and j in Frame2) or (i in Frame3 and j in Frame3):
                            Undiscovered-=1




            

            for i in Frame3:
                for j in Frame3:
                    if i<j:
                        if (i in set1 and j in set1) or (i in set2 and j in set2) or (i in set3 and j in set3):
                            TP+=1
                        else:
                            FP+=1

            #Undiscovered=0
            for i in set3:
                for j in set3:
                    if i<j:
                        Undiscovered+=1
                        if (i in Frame1 and j in Frame1) or (i in Frame2 and j in Frame2) or (i in Frame3 and j in Frame3):
                            Undiscovered-=1

            self.canvas.itemconfigure(self.text_id,text="Score: "+str(TP*2-FP-Undiscovered))
            #self.canvas.itemconfigure(self.text_id2,text="Incorrect: "+str(FP))
            #self.canvas.itemconfigure(self.text_id3,text="Undiscovered: "+str(Undiscovered))
            #self.canvas.itemconfigure(self.text_id1,text="Level: "+str(Level))
            #print("TP=", TP, "FP=", FP, "Undiscovered=", Undiscovered)



                    #if self.canvas.coords(i)[0] >= 400 and self.canvas.coords(i)[0] <= 650 and self.canvas.coords(i)[1] >= 400 and self.canvas.coords(i)[1] <= 650:
                        #print(yes)


                      #print(self.image_1.x, self.image_1)
                
            #print(self.image_2.xpos, self.image_2.ypos)
            #print(self.image_3.xpos, self.image_3.ypos)
            #print(self.image_4.xpos, self.image_4.ypos)
            #print(self.image_5.xpos, self.image_5.ypos)
            #print(self.image_6.xpos, self.image_6.ypos)
        self.mybutton = tk.Button(self, text='Calculate your score', width=50, height=5, command=button_event)
        self.mybutton.place(x=600,y=600)
    def close(self):
        print("Application-Shutdown")
        self.master.destroy()
def main():
    app_win = tk.Tk()
    app_win.title(APP_TITLE)
    app_win.geometry("+{}+{}".format(APP_XPOS, APP_YPOS))

    #app_win.geometry("{}x{}".format(APP_WIDTH, APP_HEIGHT))
    #def button_event():
    #    print(app_win.)
#    mybutton = tk.Button(app_win, text='Calculate', command=button_event)#   mybutton.pack()
    app = Application(app_win).pack(fill='both', expand=True)
    app_win.mainloop()
if __name__ == '__main__':
    main()