dia = int(input())
mes = int(input())
ano = int(input())

verificador = 0

if((mes is 4 or mes is 6 or mes is 9 or mes is 11) and dia <= 30):
    verificador += 1
elif(mes <= 12):
    if(mes is 2 and dia is 29):
        if((ano % 400 is 0) or ((ano % 4 is 0) and (ano % 100 is not 0))):
            verificador += 1
    elif(mes is 2 and dia <= 28):
        verificador += 1
    elif(dia <= 31):
        verificador += 1

if(verificador):
    print("Valida")
else:
    print("inválida")
