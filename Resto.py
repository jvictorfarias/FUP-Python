num = int(input())
if((num % 5 == 0) and (num % 3 == 0) and not (num % 7 == 0)):
    print("sim")
else:
    print("nao")
