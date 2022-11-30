vocales_minusculas=["a", "e", "i", "o", "u"]
vocales_mayusculas=["A", "E", "I", "O", "U"]
vocales_acento=["á", "é", "í", "ó", "ú"]

oracion=str(input("Ingrese una oracion: "))
total_may=0
total_min=0
total_acento=0

for i in oracion:
    for j in vocales_mayusculas:
        if i == j:
            total_may += 1
            
    for k in vocales_minusculas:
        if i == k:
            total_min += 1

    for l in vocales_acento:
        if i == l:
            total_acento += 1

print(f"Hay {total_may} mayusculas ---  Hay {total_min} minusculas --- Hay {total_acento} acentos")