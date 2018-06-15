dias = int(input())
acessos = []
cont = 0
contDias = 0
for i in range(0, dias, 1):
    acessos.append(int(input()))
for k in range(0, dias, 1):
    cont += acessos[k]
    contDias += 1
    if(cont >= 1000000):
        print contDias
        break
