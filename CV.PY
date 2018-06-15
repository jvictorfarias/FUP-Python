string = raw_input()

for i in range(0, len(string), 1):
    if string[i] == 'a' or string[i] == 'e' or string[i] == 'i'\
       or string[i] == 'o' or string[i] == 'u' or string[i] == 'A'\
       or string[i] == 'E' or string[i] == 'I'\
       or string[i] == 'O' or string[i] == 'U':
        string = string.replace(string[i], 'v')
    elif string[i] == ' ' or string[i] == 'v':
        pass
    else:
        string = string.replace(string[i], 'c')
print string
