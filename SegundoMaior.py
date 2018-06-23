lista = raw_input().split(' ')
lista = [int(i) for i in lista]
maior = lista[0]


for i in lista:
    if i > maior:
        maior = i
lista.remove(maior)
maior = lista[0]
for j in lista:
    if j > maior:
        maior = j
print maior
