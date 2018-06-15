# -*- coding: utf-8 -*-
# @autor : Joao Victor Farias
from random import randint
tamanho = int(input())
vogais_s = 'aeiou'
vogais_l = list(vogais_s)
consoantes_s = 'bcdfghjklmnpqrstvwxyz'
consoantes_l = list(consoantes_s)
indices = []
forca_jogo = ''
forca = ''
foram = []
# Forma a palavra com as vogais e consoantes nos índices pares e ímpares
for i in range(0, tamanho, 1):
    if i % 2:
        forca += vogais_l[randint(0, len(vogais_l) - 1)]
    else:
        forca += consoantes_l[randint(0, len(consoantes_l) - 1)]
for i in range(0, len(list(forca)), 1):
    forca_jogo += '_'
# Enquanto tiver '_' na forca, o programa irá rodar
while(forca_jogo.find('_') != -1):
    print ' '.join(forca_jogo)
    if len(foram):
        print '\t\tLetras que já foram : %s' % (' '.join(foram))
    listaForca = list(forca_jogo)  # Transforma a string em lista
    chute = raw_input('\nDigite seu chute : ')
    foram.append(chute)
    # Verifica em quais índices estão a letra
    for j in range(0, len(forca), 1):
        if forca.find(chute, j, len(forca)) != -1:
            j = forca.find(chute, j, len(forca))
            indices.append(forca.find(chute, j, len(forca)))
        else:
            break
    if len(indices) == 0:  # Se não achou índice, foi uma letra errada
        print 'Não acertou!'
        continue
    else:
        print 'Acertou!'
    for k in indices:
        listaForca[k] = chute
    forca_jogo = ''.join(listaForca)  # Transforma a lista em string
    indices[:] = []  # Zera a lista de índices para a proxima iteração
print '\nPalavra completa : %s' % (' '.join(forca))
