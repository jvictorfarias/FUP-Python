def anulaEspacos(string):
    count = 0
    aux = ''
    for i in range(0, len(string), 1):
        if string[i] is ' ':
            aux += string[count:i + 1]
            while(string[i] is ' '):
                count = i
                i += 1
            count += 1

        if (i + 1) - len(string) is 0:
            aux += string[count:i + 1]
            while(string[i] is ' '):
                count = i
                i += 1
            count += 1
    print(aux)


anulaEspacos(raw_input())
