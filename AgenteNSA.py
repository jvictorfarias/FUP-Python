frase = raw_input()
palavra = raw_input()
confirma = 0
j = 0

for i in palavra:
    if frase.find(i, j, len(frase)) != -1:
        confirma = 1
        j = frase.find(i, j, len(frase))
    else:
        confirma = 0
        break
    j += 1

if confirma:
    print 'Sim'
else:
    print 'Nao'
