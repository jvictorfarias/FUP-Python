from math import pow
num = int(input())
lista = raw_input()
lista = lista.split(" ")
listaInt = int(x) for x in lista

soma = 0
i = 0
j = num - 1
while(i < j):
    soma += (listaInt[i] - listaInt[j])**2
    i += 1
    j -= 1
print (soma)
    
    