# -*- coding: utf-8 -*-
from random import randint

# Listas principais :
chute = []  # Entrada do usuário
sort = []  # Números sorteados
acertos = []  # Números acertados

# Verifica se o número está no intervalo.


def verificaChute(num, lista):
    if 1 <= num <= 60 and not contains(num, lista):
        return 1
    else:
        return 0

# Função que verifica se a lista já contem o elemento.


def contains(num, lista):
    for i in lista:
        if num == i:
            return 1  # Tem o elemento
    return 0  # Não tem o elemento


# Essa parte recebe o chute e valida ele.
print('***************** MEGA SENA ******************')
while(len(chute) < 6):
    var = int(input('Digite o número de aposta  %d : ' % (len(chute) + 1)))
    if verificaChute(var, chute):
        chute.append(var)
    else:
        print('---------Número inválido ! Digite novamente !--------')
        continue

print('\n\----------- Chute válido, sorteando os números -----------/')

# Parte que sorteia os números, não sendo eles repetidos.
while(len(sort) < 6):
    var = randint(1, 60)
    if not contains(var, sort):
        sort.append(var)
    else:
        continue

# Verifica os acertos.
for i in range(0, len(chute), 1):
    if contains(chute[i], sort):
        acertos.append(chute[i])
    else:
        continue

# Mostrar números sorteados e os que você acertou.
print('Números sorteados:'),
for i in sort:
    print(i),

# Mostra o resultado.
if len(acertos) == 0:
    print('\nAzarado!')
elif len(acertos) == 1:
    print('\nFalta de sorte! :'),
    for i in acertos:
        print(i),
elif len(acertos) == 2:
    print('\nDupla! :'),
    for i in acertos:
        print(i),
elif len(acertos) == 3:
    print('\nTerno! :'),
    for i in acertos:
        print(i),
elif len(acertos) == 4:
    print('\nQuadra! :'),
    for i in acertos:
        print(i),
elif len(acertos) == 5:
    print('\nQuina! :'),
    for i in acertos:
        print(i),
else:
    print('\nMEGA! :'),
    for i in acertos:
        print(i),
