n = int(input())
for x in range(0, n + 1):
    if x < n:
        if x % 2 is 0:
            print(x)
    else:
        break
else:
    print("For finalizado")