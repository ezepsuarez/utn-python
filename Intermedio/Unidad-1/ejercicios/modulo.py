def darresultado(lista_numero):
    for x in lista_numero:
        if (int(x) % 2) == 0:
            print(f"{x} Es multiplo de 2")
        else:
            print(f"{x} NO es multiplo de 2")
