n = int(input())
j = 0
for i in range(0, n, 1):
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    if((nota1 + nota2 + nota3)/3.0) >= 7 :
        j += 1
print(j)