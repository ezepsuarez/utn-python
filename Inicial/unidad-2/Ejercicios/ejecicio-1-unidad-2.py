import sys

variable1 = (sys.argv[1])
variable2 = (sys.argv[2])
variable3 = (sys.argv[3])

print ("Variable1 es:", variable1)
print ("Variable2 es:", variable2)
print ("Variable3 es:", variable3)

resultado1= float(variable1) % 2
resultado2= float(variable2) % 2
resultado3= float(variable3) % 2

if resultado1 == 0:
    print("Resultado1 es multiplo de 2")
else:
    print("resultado1 no es multiplo de 2")

if resultado2 == 0:
    print("Resultado2 es multiplo de 2")
else:
    print("resultado2 no es multiplo de 2")

if resultado3 == 0:
    print("Resultado3 es multiplo de 2")
else:
    print("resultado3 no es multiplo de 2")