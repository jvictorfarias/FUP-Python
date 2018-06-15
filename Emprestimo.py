emprestimo = float(input())
meses = int(input())
salario = float(input())

prestacao = emprestimo / (meses * 1.0)
if(prestacao > (salario * 0.3)):
    print("nao")
else:
    print("sim")
