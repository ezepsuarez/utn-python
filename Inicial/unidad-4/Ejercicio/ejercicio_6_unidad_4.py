lista_numeros=[3, 44, 21, 78, 5, 56, 9]
resultado_mayor=[]
resultado_menor=[]

def esta_en_lista(valor):
    for i in resultado_mayor:
        if ( i == valor):
            return True

def ordenar_menor(lista):
    for e in reversed(list(enumerate(resultado_mayor))):
        resultado_menor.append(e)

def ordenar_mayor(lista):
    cantidad_elementos=len(lista)
    max=0
    for i in range(cantidad_elementos):
        for j in lista:
            if ((j > max) and (esta_en_lista(j) != True)):
                max=j
        resultado_mayor.append((max))
        max=0
    
    ordenar_menor(resultado_mayor)

print ("Lista Original: ", lista_numeros)
ordenar_mayor(lista_numeros)
print ("Lista Ordenada Mayor: ", resultado_mayor)
print ("Lista Ordenada Menor: ", resultado_menor)


""" Variante del ejercicio"""

lista = [3, 44, 21, 78, 5, 56, 9]

for i in range(1,len(lista)):
    for a in range(len(lista) - i):
        if lista[a] > lista[a+1]:
            t = lista[a]
            lista[a] = lista[a+1]
            lista[a+1] = t

print("Lista ordenada", lista)