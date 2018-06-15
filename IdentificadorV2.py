d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())
d5 = int(input())

verificador = 0

if(d3 is d1 + d2):
    if (((d4 % 2 is 0) and (d4 is 2 * d2)) or ((d4 % 2 is not 0 ) and (d4 is 2 * d2 + 1))):
        if (((d5 % d3 is 0) and (d5 is 2 * d3)) or ((d5 % d3 is not 0) and (d5 is 2 * d3 - 1))):
             verificador += 1

if(verificador):
    print("SIM")
else:
    print("NAO")