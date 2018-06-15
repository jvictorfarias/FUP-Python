chute = float(input())
MaiorMenor = input()
preco = float(input())

if(chute == preco):
    print("primeiro")
elif(MaiorMenor == 'M'):
    if(chute > preco):
        print("primeiro")
    else:
        print("segundo")
else:
    if(chute < preco):
        print("primeiro")
    else:
        print("segundo")


