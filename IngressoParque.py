filho1 = int(input())
filho2 = int(input())
filho3 = int(input())
filho4 = int(input())
price = float(input())

total = 0
somaDesconto = 0

while(somaDesconto <= 40):
    if(filho1 <= 5):
        total += price - (0.2 * price)
        somaDesconto += 20
    elif(filho1 <= 7):
        total += price - (0.15 * price)
        somaDesconto += 15
    elif(filho1 <= 10) :
        total += price - (0.05 * price)
        somaDesconto += 5
    else:
        total += price

    if(filho2 <= 5):
        total += price - (0.2 * price)
        somaDesconto += 20
    elif(filho2 <= 7):
        total += price - (0.15 * price)
        somaDesconto += 15
    elif(filho2 <= 10) :
        total += price - (0.05 * price)
        somaDesconto += 5
    else:
        total += price

    if(filho3 <= 5):
        total += price - (0.2 * price)
        somaDesconto += 20
    elif(filho3 <= 7):
        total += price - (0.15 * price)
        somaDesconto += 15
    elif(filho3 <= 10) :
        total += price - (0.05 * price)
        somaDesconto += 5
    else:
        total += price

    if(filho4 <= 5):
        total += price - (0.2 * price)
        somaDesconto += 20
    elif(filho4 <= 7):
        total += price - (0.15 * price)
        somaDesconto += 15
    elif(filho4 <= 10) :
        total += price - (0.05 * price)
        somaDesconto += 5
    else:
        total += price

    break

print('%.2f' % total)
