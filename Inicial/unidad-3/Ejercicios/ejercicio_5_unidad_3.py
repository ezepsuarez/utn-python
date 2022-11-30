cliente=input("Ingrese su nombre: ")
total=0
cantidad=1

while cantidad > 0:
    cantidad=int(input("Ingrese cantidad: "))
    if cantidad == 0:
        break
    importe=int(input("Ingrese importe: "))

    total += importe * cantidad 

print(f"Total gastado por el cliente {cliente} es: {total} Pesos")