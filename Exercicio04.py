salario = float(input("Digite o valor do salário: "))
valorPrestacao = float(input("Digite o valor da prestação do empréstimo: "))

porcentagemSalario = salario * 0.2

if valorPrestacao > porcentagemSalario:
    print("Empréstimo não concedido.")
else: 
    print("Empréstimo concedido.")