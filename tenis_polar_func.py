def tenis_polar(string):
    aux = ''
    for i in range(0, len(string), 1):
        if string[i] == 't':
            aux += 'p'
        elif string[i] == 'e':
            aux += 'o'
        elif string[i] == 'n':
            aux += 'l'
        elif string[i] == 'i':
            aux += 'a'
        elif string[i] == 's':
            aux += 'r'
        elif string[i] == 'p':
            aux += 't'
        elif string[i] == 'o':
            aux += 'e'
        elif string[i] == 'l':
            aux += 'n'
        elif string[i] == 'a':
            aux += 'i'
        elif string[i] == 'r':
            aux += 's'
        else:
            aux += string[i]
    return aux


print(tenis_polar(raw_input()))
