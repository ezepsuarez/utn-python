class Vehiculo():
    def __init__(self, color, matricula, velocidad_maxima):
        self.color = color
        self.matricula = matricula
        self.velocidad_maxima = velocidad_maxima

auto1=Vehiculo("azul", "pmp061","176")
auto2=Vehiculo("rojo", "AB993SE","256")
auto3=Vehiculo("amarillo", "abs993","376")
print(f"Vehiculo Color {auto1.color} - Matricula: {auto1.matricula} - Velocidad Maxima: {auto1.velocidad_maxima}")
print(f"Vehiculo: Color {auto2.color} - Matricula: {auto2.matricula} - Velocidad Maxima: {auto2.velocidad_maxima}")
print(f"Vehiculo: Color {auto3.color} - Matricula: {auto3.matricula} - Velocidad Maxima: {auto3.velocidad_maxima}")
