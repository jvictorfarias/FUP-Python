from random import randint
cont = 0
limiteInferior = 0
limiteSuperior = 1025
while(True):
    guess = randint(limiteInferior + 1, limiteSuperior - 1)
    cont += 1
    print(guess)
    correcao = raw_input()
    if correcao == 'acertou':
        break
    elif correcao == 'menor':
        limiteInferior = guess
    else:
        limiteSuperior = guess


print("Acertei")
print(cont)
