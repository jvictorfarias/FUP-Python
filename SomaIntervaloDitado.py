n = int(input())
somaPar = 0
somaImpar = 0
for x in range(1, n + 1, 1):
    aux = int(input())
    if aux % 2 is 0:
        somaPar += aux
    else:
        somaImpar += aux
print(somaPar, somaImpar)
