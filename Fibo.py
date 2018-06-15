fibo = int(input())
fibA = 1
fibB = 1
aux = 0
print fibA
print fibB
for i in range(2, fibo, 1):
    aux = fibA
    fibA = fibA + fibB
    fibB = aux
print fibA
