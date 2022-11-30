def perimetro (valor_radio):
    valor_pi= 3.1416
    print ("Radio es: ", valor_radio)
    perimetro= 2 * 3.1416 * int(valor_radio)
    print ("Longitud del perimetro es: ", perimetro)

def area (valor_radio):
    valor_pi= 3.1416
    valor_radioal2 = int(valor_radio) * int(valor_radio)
    areatotal= valor_pi * valor_radioal2
    print ("Area es: ", areatotal)

def porcentaje (valor):
    print("Este es el valor incrementando en un 10%", (int(valor)*1.10))

print ("Para calcular la longitud del perimetro elija [ 1 ]")
print ("Para calcular el area de la circunferencia elija [ 2 ]")
print ("Para calcular el 10 % de un mumero elija [ 3 ]")

eleccion=int(input("Ingrese la opcion elegida: "))

if eleccion == 1:
    valor_radio = input("Ingrese el radio de la circunferencia: ")
    perimetro (valor_radio)
elif eleccion == 2:
    valor_radio = input("Ingrese el radio de la circunferencia: ")
    area (valor_radio)
elif eleccion == 3:
    valor = input("Ingrese un valor: ")
    porcentaje (valor)
