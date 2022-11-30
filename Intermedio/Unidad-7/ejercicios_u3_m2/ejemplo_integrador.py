import os
import datetime

class RegistroLogError(Exception):

    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    ruta = os.path.join(BASE_DIR, "log.txt")

    def __init__(self, linea, archivo, fecha):
        self.linea = linea
        self.archivo = archivo
        self.fecha = fecha

    def registrar_error(self):
        log = open(self.ruta, "a")
        print("Se ha dado un error:", self.archivo, self.linea, self.fecha, file=log)

def registrar():
    print("------>>>> Registro")
    raise RegistroLogError(7, "daaaa.txt", datetime.datetime.now())
try:
    print ("try")
    registrar()
except RegistroLogError as log:
    print("aca error")
    log.registrar_error()