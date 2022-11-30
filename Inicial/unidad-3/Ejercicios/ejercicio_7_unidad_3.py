cliente=input("Ingrese su nombre: ")
productos_comprados={}
total=0
cantidad=1

while cantidad > 0:
    cantidad=int(input("Ingrese cantidad: "))
    if cantidad == 0:
        break
    producto=str(input("Ingrese el producto:"))

    importe=int(input("Ingrese importe: "))
    productos_comprados = { "cantidad" : cantidad , "importe": importe}
    total += importe * cantidad

print("Productos comprados:")
print(productos_comprados)
print(f"Total gastado por el cliente {cliente} es: {total} Pesos")