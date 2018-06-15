string = raw_input()
count = 0
aux = ' '
for i in range(0, len(string), 1):
    if string[i]  is ' ':
        aux += string[count:i][::-1] + ' '
        count = i
    if (i+1) - len(string) is 0:
        aux += string[count+1:len(string)][::-1]
print(aux)
