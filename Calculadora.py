primeiroNum = int(input())
segundoNum = int(input())
opc = input()

if(opc == "+"):
    print(primeiroNum + segundoNum)
elif(opc == "-"):
    print(primeiroNum - segundoNum)
elif(opc == "*"):
    print(primeiroNum * segundoNum)
elif(opc == "/"):
    if (segundoNum == 0):
        print("invalida")
    else:
        print(primeiroNum / segundoNum)
else:
    print("invalida")
