notas = [input(), input(), input()]
trab = float(input())

notas.remove(min(notas))
media = ((notas[0] + notas[1] + trab) / 3 * 1.0)
if(media >= 7.0):
    print("Aprovado com %.1f" % (media))
else:
    print("Final com %.1f" % (media))

