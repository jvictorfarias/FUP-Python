def calcula_idade_completa(dataNasc, dataAtual):
    dataNasc = [int(i) for i in dataNasc]
    dataAtual = [int(i) for i in dataAtual]
    # Anos
    if dataNasc[1] > dataAtual[1]:
        anos = dataAtual[2] - dataNasc[2] - 1
    elif dataNasc[1] == dataAtual[1]:
        if dataNasc[0] > dataAtual[0]:
            anos = dataAtual[2] - dataNasc[2] - 1
        else:
            anos = dataAtual[2] - dataNasc[2]
    else:
        anos = dataAtual[2] - dataNasc[2]
    # Meses
    if dataAtual[1] - dataNasc[1] < 0:
        meses = 12 + dataAtual[1] - dataNasc[1]
    else:
        meses = dataAtual[1] - dataNasc[1]
    # Dias
    if dataAtual[0] < dataNasc[0]:
        dias = dataAtual[0] - dataNasc[0] + 31
    else:
        dias = dataAtual[0] - dataNasc[0]

    return anos, meses, dias


print '%d anos %d meses % dias' % (calcula_idade_completa(raw_input()))
