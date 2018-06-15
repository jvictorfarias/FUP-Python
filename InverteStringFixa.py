string = raw_input()
aux = ''
for i in range(0, len(string), 1):
    if string[i] == string[i].upper():
        aux += string[i].lower()
    elif string[i] == string[i].lower():
        aux += string[i].upper()
    else:
        aux += ' '
print aux
