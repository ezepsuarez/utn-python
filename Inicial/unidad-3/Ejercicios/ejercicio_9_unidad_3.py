def alta_compra (producto, cantidad, importe):
    producto_comprado[producto] = { "cantidad" : cantidad , "importe": importe}

def consulta_compra ():
    for key, i in producto_comprado.items():
        print(f"Producto {key} -> Compra: {i}")


def baja_compra(producto):
    producto_comprado.pop(producto)

def modifica_compra(producto):
    newcant=int(input("Ingrese nueva cantidad: "))
    newprecio=int(input("Ingrese nuevo importe: "))
    producto_comprado[producto]= {"cantidad" : newcant, "importe" : newprecio}

cliente=input("Ingrese su nombre: ")
producto_comprado={}
total=0
cantidad=1

while cantidad > 0:
    cantidad=int(input("Ingrese cantidad [0] para finalizar: "))
    if cantidad == 0:
        break
    producto=(input("Ingrese el producto:"))
    importe=int(input("Ingrese importe: "))
    alta_compra(producto,cantidad,importe)

opcion='N'

print("listado del diccionario: ")
print(producto_comprado)
print("---" * 30)
while opcion != 'S':
    print(" ")
    print("Ver Productos comprados [A]")
    print("Dar de baja un producto Baja Producto [B]")
    print("Modificar compra [C]")
    print("Salir [S]")
    opcion=input("Elija su opcion: ")
    
    if opcion == "A":
        consulta_compra()

    if opcion == "B":
        producto=input("Ingrese el prodcuto a eliminar: ")
        baja_compra(producto)

    if opcion == "C":
        producto=input("Ingrese el prodcuto a modificar: ")
        modifica_compra(producto)
