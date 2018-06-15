a = int(input())
b = int(input())
somaPar = 0
somaImpar = 0
for x in range(a, b + 1, 1):
    if x <= b:
        if x % 2 is 0:
          somaPar += x
        else:
            somaImpar += x
    else:
        break

print(somaPar + " " + somaImpar)