segundos = int(input())
horas = segundos/3600
minutos = (segundos - ( 3600 * horas))/60
segundos = segundos - (3600 * horas) - (minutos * 60)
print("%d:%d:%d"  % (horas, minutos, segundos))
 