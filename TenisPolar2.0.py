string = raw_input()
aux = ''
tenis = 'tenis'
polar = 'polar'
salvaTenis = []
salvaPolar = []
for i in tenis:
    for k in range(0, len(string), 1):
        if string.find(i) != -1:
            salvaTenis.append(string.find(i))
            k = string.find(i)
        else:
            pass
for j in polar:
    for k in range(0, len(string), 1):
        if string.find(j) != -1:
            salvaPolar.append(string.find(j))
            k = string.find(j)
        else:
            pass
string_l = list(string)
for x in salvaTenis:
