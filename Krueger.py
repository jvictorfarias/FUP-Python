def contaVogal(string):
    j = 0
    cont = 0
    auxCont = 0
    auxInd = 0
    for i in range(0, len(string), 1):
        if cont > auxCont:
            auxCont = cont
            auxInd = j - cont
        if(string[i] == 'a' or string[i] == 'e' or string[i] == 'i'
           or string[i] == 'o' or string[i] == 'u'):
            if(i + 1 - len(string) == 0):
                pass
            else:
                j = i + 1
                while(string[j] == 'a' or string[j] == 'e' or string[j] == 'i'
                      or string[j] == 'o' or string[j] == 'u' and j < len(string)):
                        j += 1
                        i = j
                        cont += 1
    return string[auxInd:auxInd + auxCont]


num = int(input())
for i in range(0, num, 1):
    string = raw_input()
    print contaVogal(string)
