dia1 = input()
mes1 = input()
ano1 = input()

dia2 = input()
mes2 = input()
ano2 = input()

if mes2 < mes1:
    print(ano2 - ano1 -1)
elif (mes1 < mes2):
    print(ano2 - ano1)
else:
    if(dia2 < dia1):
        print(ano2 - ano1 - 1)
    else:
        print(ano2 - ano1)