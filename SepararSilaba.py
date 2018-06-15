string = raw_input()
aux = ''
# paraguai
j = 0
for i in range(0, len(string), 1):
    if(string[i] == 'a' or string[i] == 'e' or string[i] == 'i'
       or string[i] == 'o' or string[i] == 'u'):
        if i + 1 - len(string) == 0:
            aux += string[j:len(string)]
        else:
            if(string[i+1] != 'a' or string[i+1] != 'e' or string[i+1] != 'i'
               or string[i+1] != 'o' or string[i] != 'u'):
                aux += string[j:i+1] + '-'
                i += 1
                j = i
print aux
