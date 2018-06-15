# charset utf-8
lado1 = input()
lado2 = input()
lado3 = input()

if((lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1)):
    print("Nao e triângulo")
elif((lado1 == lado2) and (lado2 == lado3)):
    print("Equilatero")
elif((lado1 == lado2 and lado1 is not lado3) or (lado1 == lado3 and lado1 is not lado2) or (lado2 == lado3 and lado2 is not lado1)):
    print("Isosceles")
elif(lado1 is not lado2 and lado1 is not lado3):
    print("Escaleno")
else:
    print("Done")