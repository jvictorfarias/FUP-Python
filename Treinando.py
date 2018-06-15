# coding: UTF-8
condicaoSaida = 0
while(condicaoSaida == 0):
    plano = int(input('\nDigite o seu plano :\n1-Básico\n2-Controle\n3-Conta\n'
                      '4-Sair\nDigite a opção : '))
    if(plano == 1):
        minutos = float(input('\nDigite a quantidade de minutos usados : '))
        if(minutos >= 0 and minutos <= 15):
            resultado = minutos * 0.5
            print('\nO valor do plano Básico é : %.2fR$' % (resultado))
        elif(minutos > 15 and minutos <= 30):
            resultado = minutos * 0.40
            print('\nO valor do plano Básico é  : %.2fR$' % (resultado))
        elif (minutos > 30):
            resultado = minutos * 0.30
            print('\nO valor do plano Básico é  : %.2fR$' % (resultado))
        else:
            print('\nO valor é inválido %.2f!!!!' % (minutos))
    elif(plano == 2):
        minutos = float(input('\nDigite a quantidade de minutos usados : '))
        if(minutos >= 0 and minutos <= 15):
            resultado = minutos * 0.45
            print('\nO valor do plano Controle: %.2fR$' % (resultado))
        elif(minutos > 15 and minutos <= 30):
            resultado = minutos * 0.37
            print('\nO valor do plano Controle: %.2fR$' % (resultado))
        elif (minutos > 30):
            resultado = minutos * 0.24
            print('\nO valor do plano Controle: %.2fR$' % (resultado))
        else:
            print('\nO valor é inválido %2f!!!!' % (minutos))
    elif(plano == 3):
        minutos = float(input('\nDigite a quantidade de minutos usados : '))
        if(minutos >= 0 and minutos <= 15):
            resultado = minutos * 0.40
            print('\nO valor do plano Conta : %.2fR$' % (resultado))
        elif(minutos > 15 and minutos <= 30):
            resultado = minutos * 0.32
            print('\nO valor do plano Conta : %.2fR$' % (resultado))
        elif (minutos > 30):
            resultado = minutos * 0.20
            print('\nO valor do plano Conta : %.2fR$' % (resultado))
        else:
            print('\nO valor é inválido %2f!!!!' % (minutos))
    elif(plano == 4):
        condicaoSaida = 1
        print('\nPrograma finalizado !!!\n')
    else:
        print('\nPlano inválido !!!')
