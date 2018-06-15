lista = input()
lista = lista.split(' ')
listaInt = []
listaMenor = []
listaMaior = []
for i in lista:
    listaInt.append(int(i))
num = int(input())
for id in listaInt:
    if id <= num:
        listaMenor.append(id)
    else:
        listaMaior.append(id)
if len(listaMenor) is 0:
    print(-1)
for j in listaMenor:
    print(j),
if len(listaMaior) is 0:
    print(-1)
for k in listaMaior:
    print(k),
