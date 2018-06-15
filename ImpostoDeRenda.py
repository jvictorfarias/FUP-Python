salario = float(input())
if(salario < 1000.0):
    print("isento")
elif(salario >= 1000.0 and salario < 1800.0):
    print( 0.1 * (salario - 1000))
elif(salario >= 1800.0 and salario < 3000.0):
    print(0.1 * (1800 - 1000) + 0.15 * (salario - 1800))
else:
    print(0.1 * (1800 - 1000) + 0.15 * (3000 - 1800) + 0.25 *(salario - 3000))