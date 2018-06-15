def resultado(c1, c2):
    if(c1 > c2):
        print("segundo")
    elif(c2 > c1):
        print("primeiro")
    else:
        print("empate")


preco = int(input())
chute1 = int(input())
chute2 = int(input())

c1 = preco - chute1
c2 = preco - chute2

if(c1 < 0):
    c1 *= -1
if(c2 < 0):
    c2 *= -1

resultado(c1, c2)
