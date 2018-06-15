def exists(num, lista):
    for i in lista:
        if num == i:
            return 1
    return 0


def converte_string_int(string):
    string = string.split(' ')
    listaInt = []
    for i in string:
        listaInt.append(int(i))
    return listaInt


n = int(input())
lista_um_s = raw_input()
lista_dois_s = raw_input()
lista_um = []
lista_dois = []
lista_uniao = []

lista_um = converte_string_int(lista_um_s)
lista_dois = converte_string_int(lista_dois_s)

for i in range(0, n, 1):
    lista_uniao.append(lista_um[i])
for i in range(0, n, 1):
    if not exists(lista_dois[i], lista_um):
            lista_uniao.append(lista_dois[i])
    else:
        continue

for i in lista_uniao:
    print(i),
