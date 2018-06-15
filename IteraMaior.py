n = int(input())
maior = 0
menor = 0

for i in range(0, n, 1):
    aux = int(input())
    if maior < aux :
        maior = aux
    elif menor > aux :
        menor = aux
    elif menor is 0 :
        menor = aux

print(menor, maior)
        