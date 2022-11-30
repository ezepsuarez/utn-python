from re import S


variable1 = input("Ingrese un valor A: ")
variable2 = input("Ingrese un valor B: ")
variable3 = input("ingrese un valor C: ")

resultado1= int(variable1) * int(variable2)
resultado2= int(resultado1) + int(variable3)

print ("El resultado de la multiplicacion de A*B es: ", int(resultado1))
print ("El resultado de la multiplicacion de (A*B) +C es: ", int(resultado2))