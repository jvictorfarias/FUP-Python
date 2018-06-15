numero = int(input())
aux = 0
pali = 0
cont = 1

for i in range(0, numero, 1):
    if numero > 9 and cont is 1:
        aux = numero % 10
        pali += aux * cont
        numero /= numero
        cont += 9
    elif numero > 9 :
        aux = numero % 10
        pali += aux * cont
        numero /= numero
        cont += 10
    else:
        break

print(pali)
