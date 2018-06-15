def calcula_idade(dataNascimento, dataAtual):
    dataNascimento = [int(i) for i in dataNascimento]
    dataAtual = [int(i) for i in dataAtual]

    calculaIdade = dataAtual[2] - dataNascimento[2]
    if dataAtual[1] < dataNascimento[1]:
        calculaIdade -= 1
    elif dataAtual[1] == dataNascimento[1]:
        if dataAtual[0] <= dataNascimento[0]:
            calculaIdade -= 1
    return calculaIdade


print(calcula_idade(raw_input().split('/'), raw_input().split('/')))
