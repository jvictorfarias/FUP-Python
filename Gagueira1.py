string = raw_input()
aux = ''
j = 0
for i in range(0, len(string), 1):
    if string[i] == ' ':
        aux += string[j:i] + ' ' + string[j:i] + ' '
        j = i + 1
    elif (i + 1 - len(string)) == 0:
        aux += string[j:len(string)] + ' ' + string[j:len(string)]
print aux
