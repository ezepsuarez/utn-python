class Vehiculo():
    def __init__(self, color, matricula, velocidad_maxima):
        self.color = color
        self.matricula = matricula
        self.velocidad_maxima = velocidad_maxima

    def imprimir (self,):
        print(f"Vehiculo: Color {self.color} - Matricula: {self.matricula} - Velocidad Maxima: {self.velocidad_maxima}")

auto1=Vehiculo("azul", "pmp061","176")
auto2=Vehiculo("rojo", "AB993SE","256")
auto3=Vehiculo("amarillo", "abs993","376")
auto1.imprimir()
auto2.imprimir()
auto3.imprimir()
