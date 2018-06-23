def numerologia(nome):
    count_num = 0
    for i in range(0, len(nome), 1):
        if i < len(nome) - 2:
            if eh_vogal(nome[i]):
                count_num += eh_vogal(nome[i])
            elif nome[i] == ' ':
                pass
            elif not eh_vogal(nome[i]):
                if not eh_vogal(nome[i + 1]):
                    pass
                elif eh_vogal(nome[i+2]) and nome[i+1] == ' ':
                    count_num += ((i+1) * eh_vogal(nome[i + 2]))
                else:
                    count_num += ((i+1) * eh_vogal(nome[i + 1]))
        else:
            if eh_vogal(nome[i]):
                count_num += eh_vogal(nome[i])
            else:
                pass
    return count_num


def eh_vogal(letra):
    if letra == 'a':
        return 1
    elif letra == 'e':
        return 2
    elif letra == 'i':
        return 3
    elif letra == 'o':
        return 4
    elif letra == 'u':
        return 5
    else:
        return 0


def main():
    nome = raw_input()
    print numerologia(nome)


main()
