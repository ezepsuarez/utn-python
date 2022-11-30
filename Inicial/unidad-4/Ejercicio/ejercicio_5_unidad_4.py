
def muestra_anios(edad):
    res1=""
    for x in range(1,edad+1):
        if ( x < edad):
            res1 += str(x) + ","
        else:
            res1 +=str(x)
    print (res1)
    res1=""
    for j in range(edad, 0, -1):
        if ( j == 1 ):
            res1 += str(j)
        else:
            res1 +=str(j) + ","
    print (res1)

edad=int(input("Ingrese su edad:"))
muestra_anios(edad)