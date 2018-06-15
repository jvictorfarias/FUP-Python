def get_preco_proximo(lista, preco_desejado):
    desejado = preco_desejado
    for i in lista:
        if modulo(i, preco_desejado) < modulo(desejado, preco_desejado):
            desejado = i
    return desejado


def modulo(a, b):
    if a - b >= 0:
        return a - b
    else:
        return (a - b) * -1


def main():
    none = input()
    entrada = raw_input().split(' ')
    entrada = [float(i) for i in entrada]
    print(get_preco_proximo(entrada, float(input())))


main()
