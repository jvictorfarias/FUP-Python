n = int(input())
listaNum = []
listaMenor = []
listaMaior = []
listaOrdenada = []

numeros = raw_input()
numeros = numeros.split(' ')

for i in range(0, n, 1):
    listaNum.append(int(numeros[i]))

for i in listaNum:
    if i <= listaNum[-1]:
        listaMenor.append(i)
    else:
        listaMaior.append(i)

for i in range(0, len(listaMenor) - 1, 1):
    listaOrdenada.append(listaMenor[i])

listaOrdenada.append(listaNum[-1])

for i in listaMaior:
    listaOrdenada.append(i)
for i in listaOrdenada:
    print i,
