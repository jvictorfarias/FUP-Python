from random import randint
num = randint(1, 1024)
cont = 0
while(True):
    cont += 1
    guess = int(input())
    if guess is num :
        break
    elif guess < num :
        print("Menor")
    else :
        print("Maior")
print("Acertou")
print(cont)
