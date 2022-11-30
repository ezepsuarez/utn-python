oracion=str(input("Ingrese una oracion: "))
j=0

for i in oracion:
    if (i == "a"):
        j+=1

print(f"Es la oracion: [ {oracion} ] hay {j} letra a ")