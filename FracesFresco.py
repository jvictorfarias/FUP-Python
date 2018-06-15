string = raw_input()
j = 0
aux = ''
for i in range(0, len(string), 1):
    if string[i] == ' ':
        if string[i-1] == string[i+1]:
            aux += string[j:i-1]
            j = i + 1
    elif (i + 1 - len(string) == 0):
            aux += string[j:len(string)]
print aux
