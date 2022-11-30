cliente=input("Ingrese su nombre: ")
productos_comprados=[]
total=0
cantidad=1

while cantidad > 0:
    cantidad=int(input("Ingrese cantidad: "))
    if cantidad == 0:
        break
    productos_comprados.append(input("Ingrese el producto:"))
    importe=int(input("Ingrese importe: "))

    total += importe * cantidad 
print("Productos comprados:")
print(productos_comprados)
print(f"Total gastado por el cliente {cliente} es: {total} Pesos")