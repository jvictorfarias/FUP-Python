n = int(input())
aux = n
lista = []

while(aux > 9):
    lista.append(aux % 10)
    aux = aux / 10
lista.append(aux)
lista.reverse()
