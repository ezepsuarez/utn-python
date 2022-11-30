def alta_compra (producto, cantidad, importe):
    producto_comprado.append([producto, cantidad, importe])

def consulta_compra ():
    for i in producto_comprado:
        print (i)

def baja_compra(producto):
    for i in producto_comprado:
        if i[0] == producto:
            producto_comprado.pop(producto_comprado.index(i))

def modifica_compra(producto):
    for i in producto_comprado:
        if i[0] == producto:
            newcant=int(input("Ingrese nueva cantidad: "))
            newprecio=int(input("Ingrese nuevo importe: "))
            indice=producto_comprado.index(i)
    producto_comprado[indice] = (producto, newcant, newprecio)

cliente=input("Ingrese su nombre: ")
producto_comprado=[]
total=0
cantidad=1

while cantidad > 0:
    cantidad=int(input("Ingrese cantidad [0] para finalizar: "))
    if cantidad == 0:
        break
    producto=(input("Ingrese el producto:"))
    importe=int(input("Ingrese importe: "))
    total += importe * cantidad 
    alta_compra(producto,cantidad,importe)

opcion='N'

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
