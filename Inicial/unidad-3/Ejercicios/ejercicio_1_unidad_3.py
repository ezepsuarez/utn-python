lista_numero=[]
rango=int(input("Ingrese la cantidad de numeros a evaluar: "))

for i in range(rango):
    lista_numero.append(int(input("Ingrese un numero: ")))

for x in lista_numero:
    if (int(x) % 2) == 0:
        print(f"{x} Es multiplo de 2")
    else:
        print(f"{x} NO es multiplo de 2")
