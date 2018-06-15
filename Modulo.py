# coding: UTF-8
def modulo(num):
    return num * -1


num = int(input("Digite o número : "))
if(num < 0):
    print(modulo(num))
else:
    print(num)
