n = int(input())
lista = []
flag = 0
string = raw_input()
string = string.split(' ')
string = list(string)
for i in range(0, n, 1):
    lista.append(int(string[i]))
for j in range(0, n - 2, 1):
    if lista[j] > lista[j + 1]:
        flag += 1
if flag:
    print('Precisa de ajuste')
else:
    print('ok')
