# coding: UTF-8
def verifica(num):
    if(num > 0):
        print("positivo")
    elif(num < 0):
        print("negativo")
    else:
        print("nulo")


num = int(input("Digite um número inteiro : "))
verifica(num)
