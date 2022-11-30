class Vehiculo():
    def __init__(self, color, matricula, velocidad_maxima):
        self.color = color
        self.matricula = matricula
        self.velocidad_maxima = velocidad_maxima

    def imprimir (self,):
        print(f"Vehiculo: Color {self.color} - Matricula: {self.matricula} - Velocidad Maxima: {self.velocidad_maxima}")

class Tren(Vehiculo):
    def __init__(self, color, matricula, velocidad_maxima, peso):
        super().__init__(color, matricula, velocidad_maxima)
        self.peso = peso

    #Uso de polimorfismo
    def imprimir (self,):
        print(f"Tren: Color {self.color} - Matricula: {self.matricula} - Velocidad Maxima: {self.velocidad_maxima} - Peso: {self.peso}")
        

tren1=Tren("celeste", "F1","100","2T")
tren2=Tren("violeta", "F2","120","10T")
tren3=Tren("naranja", "F3","250","30T")
tren1.imprimir()
tren2.imprimir()
tren3.imprimir()
