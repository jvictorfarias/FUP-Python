valorEmprestimo = float(input())
meses = int(input())
salario = float(input())
emprestimoTomado = float(input())

if((valorEmprestimo / meses + emprestimoTomado) < (salario * 0.3)):
    print("SIM")
else:
    print("NAO")