salarioAtual = float(input())

if (salarioAtual <= 1000.00):
    salarioAtual = salarioAtual + (salarioAtual * 0.2)
elif (salarioAtual <= 1500.00):
    salarioAtual = salarioAtual + (salarioAtual * 0.15)
elif (salarioAtual <= 2000.00):
    salarioAtual = salarioAtual + (salarioAtual * 0.1)
else:
    salarioAtual = salarioAtual + (salarioAtual * 0.05)

print('%.2f' % salarioAtual)
