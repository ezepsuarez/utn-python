import datetime
import calendar

edad=int(input("Ingrese su edad: "))
anio=datetime.datetime.today().year
rango=int(anio)-edad +1

for i in range (rango, anio):
    print ("Cumplio años en", i)