numCompetidores = int(input())
contador = 0
ganhador = 0
pedraMaisProxima = 0 

while(contador < numCompetidores):
    pedra1 = input()
    pedra2 = input()

    if((pedra1 - 10) > 0 and (pedra2 - 10) > 0):
        if(pedra1 < pedra2):
            if((pedra1 * -1) < pedraMaisProxima):
                pedraMaisProxima = pedra1
                ganhador = contador
        else:
            if((pedra2 * -1) < pedraMaisProxima):
                pedraMaisProxima = pedra2
                ganhador = contador
    contador += 1

if(ganhador == 0):
    print("sem ganhador")
else:
    print(ganhador)