def calculaIMC(peso, altura):
    return peso / (pow(altura, 2))


peso = float(input())
altura = float(input())
resultado = calculaIMC(peso, altura)

if(resultado < 17):
    print("muito abaixo do peso")
elif(resultado >= 17 and resultado <= 18.49):
    print("abaixo do peso")
elif(resultado > 18.49 and resultado <= 24.99):
    print("peso normal")
elif(resultado > 24.99 and resultado <= 29.99):
    print("acima do peso")
elif(resultado > 29.99 and resultado <= 34.99):
    print("obesidade")
elif(resultado > 34.99 and resultado <= 39.99):
    print("obesidade severa")
else:
    print("obesidade morbida")
