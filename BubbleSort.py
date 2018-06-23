lista = raw_input().split(' ')
lista = [int(i) for i in lista]
trocou = True
while(trocou):
    trocou = False
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            trocou = True
print lista
