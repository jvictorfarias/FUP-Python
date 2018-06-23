def calcula_intervalo(lista, a, b):
    somatorio = 0
    for i in lista:
        if a <= i <= b:
            somatorio += i
    return somatorio


def main():
    lista = raw_input().split(' ')
    lista = [int(i) for i in lista]
    intervalo = raw_input().split(' ')
    intervalo = [int(j) for j in intervalo]
    print calcula_intervalo(lista, intervalo[0], intervalo[1])


main()
