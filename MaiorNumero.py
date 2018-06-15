# coding: UTF-8
def verificaMaiorNumero(num1, num2):
    if (num1 > num2):
        return num1
    else:
        return num2


num1 = int(input())
num2 = int(input())
print(verificaMaiorNumero(num1, num2))
