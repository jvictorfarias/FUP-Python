# coding: UTF-8
plano = int(input())
minutos = float(input())

if(plano == 1):
    if(minutos >= 0 and minutos <= 15):
        resultado = minutos * 0.5
        print((resultado))
    elif(minutos > 15 and minutos <= 30):
        resultado = minutos * 0.40
        print((resultado))
    elif (minutos > 30):
        resultado = minutos * 0.30
        print((resultado))
elif(plano == 2):
    if(minutos >= 0 and minutos <= 15):
        resultado = minutos * 0.45
        print(resultado)
    elif(minutos > 15 and minutos <= 30):
        resultado = minutos * 0.37
        print(resultado)
    elif (minutos > 30):
        resultado = minutos * 0.24
        print((resultado))
elif(plano == 3):
    if(minutos >= 0 and minutos <= 15):
        resultado = minutos * 0.40
        print((resultado))
    elif(minutos > 15 and minutos <= 30):
        resultado = minutos * 0.32
        print((resultado))
    elif (minutos > 30):
        resultado = minutos * 0.20
        print((resultado))
