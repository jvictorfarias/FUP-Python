num = int(input())
num1 = []
num1Int = 0
num2 = []
num2Int = 0
expoente = num - 1
for i in range(0, num, 1):
    num1.append(int(input()))
for k in range(0, num, 1):
    num2.append(int(input()))
for j in range(0, num, 1):
    num1Int += num1[j] * (10**expoente)
    num2Int += num2[j] * (10**expoente)
    expoente -= 1
print num1Int + num2Int
