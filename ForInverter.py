string = 'teste'
j = len(string)
aux = ''
for k in range(0, len(string), 1):
    aux += string[j - 1]
    j -= 1
print(aux)