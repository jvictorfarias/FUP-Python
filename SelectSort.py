lista = raw_input().split(' ')
lista = [int(i) for i in lista]
index = 0
for i in range(0, len(lista), 1):
    menor = i
    for j in range(i + 1, len(lista), 1):
        if lista[j] < lista[menor]:
            menor = j
        else:
            continue
    lista[i], lista[menor] = lista[menor], lista[i]
print lista
