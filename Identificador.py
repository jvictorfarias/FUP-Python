d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())
d5 = int(input())

verificador = 0

if((d1 % 2 is not 0) and (d3 % 2 is not 0) and (d5 % 2 is not 0)):
    if ((d2 % 2 is 0) and (d4 % 2 is 0)):
        if((d1 + 4 is d3) and (d3 + 2 is d5)):
            verificador += 1

if(verificador):
    print("SIM")
else:
    print("NAO")
