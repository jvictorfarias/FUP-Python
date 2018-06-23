def get_maior_variacao(preco_ant, preco_atual):
    maior = variacao_preco(preco_ant[0], preco_atual[0])
    count = 0
    for i in range(1, len(preco_ant)):
        if variacao_preco(preco_ant[i], preco_atual[i]) > maior:
            maior = variacao_preco(preco_ant[i], preco_atual[i])
            count = i
        else:
            continue
    return count


def variacao_preco(preco_ant, preco_atual):
    return modulo(100 * (preco_atual - preco_ant) / preco_ant)


def modulo(valor):
    if valor < 0:
        return valor * -1
    else:
        return valor


def main():
    flawless = input()
    preco_ant = raw_input().split(' ')
    preco_ant = [float(i) for i in preco_ant]
    preco_atual = raw_input().split(' ')
    preco_atual = [float(i) for i in preco_atual]
    print get_maior_variacao(preco_ant, preco_atual)


main()
