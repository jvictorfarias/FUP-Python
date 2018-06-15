opc = str(input())
jog1 = int(input())
jog2 = int(input())

if(opc == 'p'):
    if (jog1 % jog2 == 0):
        print("Venceu")
    else:
        print("Perdeu")
else:
    if (jog1 % jog2 == 0):
        print("Perdeu")
    else:
        print("Venceu")
