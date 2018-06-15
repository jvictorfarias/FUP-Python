# -*- coding: utf-8 -*-
from random import randint

# Listas principais :
chute = []  # Entrada do usuário
sort = []  # Números sorteados
acertos = []  # Números acertados

# Verifica se o número está no intervalo.


def verificaChute(chute):
    for i in chute:
        if 1 <= i <= 60 and contaLista(i, chute):
            continue
        else:
            return 0
    return 1

# Função que verifica se a lista já contem o elemento.


def contains(num, lista):
    for i in lista:
        if num == i:
            return 1  # Tem o elemento
    return 0  # Não tem o elemento


# Função que verifica se o número já existe na lista mais de 1 vez, que é uma
# versão estendida da 'contains', mas já que a especificação do moodle é
# corrigir a entrada após ter recebido, fiz essa função pra corrigir os números
# contando que já existe 1 e não pode ter mais de 1.

def contaLista(num, lista):
    count = 0
    for i in lista:
        if num == i:
            count += 1
            if count > 1:
                return 0
    return 1


# Essa parte recebe o chute e valida ele.
print('***************** MEGA SENA ******************')
while(True):
    for i in range(0, 6, 1):
        chute.append(int(input('Digite o número de aposta % d : ' % (i + 1))))
    if verificaChute(chute):
        print('\n\----------- Chute válido, sorteando os números -----------/')
        break
    else:
        print('---------Número inválido ! Digite novamente !--------')
        while(len(chute) > 0):
            chute.pop()  # Se a lista for inválida, esvazia ela.
        continue

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
print('\nNúmeros que você acertou:'),
if len(acertos):
    for i in acertos:
        print(i),
else:
    print('Nenhum!'),

# Mostra o resultado.
if len(acertos) == 0:
    print('\n\t------------Azarado!-----------')
elif len(acertos) == 1:
    print('\n\t----------Falta de sorte!----------')
elif len(acertos) == 2:
    print('\n\t----------Dupla!------------')
elif len(acertos) == 3:
    print('\n\t---------Tripla!------------')
elif len(acertos) == 4:
    print('\n\t---------Quadra!------------')
elif len(acertos) == 5:
    print('\n\t----------Quina!------------')
else:
    print('\n\t!!!!!!!!!!!MEGA!!!!!!!!!!!!!')
