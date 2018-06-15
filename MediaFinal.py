nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = (nota1 + nota2 + nota3) / 3
if(media >= 7.0):
    print("Aprovado")
elif(media >= 4.0):
    notaAF = float(input())
    if(notaAF >= 5.0):
        if (((notaAF + media) / 2) >= 5):
            print("Aprovado")
        else:
            print("Reprovado")
    else:
        print("Reprovado")
else:
    print("Reprovado")