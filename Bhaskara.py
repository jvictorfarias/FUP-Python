# coding: UTF-8
from math import sqrt

a = int(input('Digite o a : '))
b = int(input('Digite o b : '))
c = int(input('Digite o c : '))

primeiraRaiz = ((- b + sqrt((b * b) - 4 * a * c)) / 2 * a)
segundaRaiz = ((- b - sqrt((b * b) - 4 * a * c)) / 2 * a)

print('A primeira raiz é : %d\n'
      'A segunda raiz é : %d' % (primeiraRaiz, segundaRaiz))
