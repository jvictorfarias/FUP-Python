def combina(lista_um, lista_dois):
    lista_tres = []
    for i in range(0, len(lista_um), 1):
        lista_tres.append(lista_um[i])
        lista_tres.append(lista_dois[i])
    return lista_tres


def main():
    lista_um = raw_input().split(' ')
    lista_dois = raw_input().split(' ')
    lista_um = [int(x) for x in lista_um]
    lista_dois = [int(x) for x in lista_dois]
    print combina(lista_um, lista_dois)


main()
