print("Escolha a opção: ")
print("1- Soma de 2 números.")
print("2- Diferença entre 2 números (maior pelo menor).")
print("3- Produto entre 2 números.")
print("4- Divisão entre 2 números (o denominador não pode ser zero).")

opcao = int(input("\nEscolha uma opção: "))
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if opcao == 1:
    print(f"{numero1} + {numero2} = {numero1 + numero2}")
elif opcao == 2:
    if numero1 > numero2:
        print(f"{numero1} - {numero2} = {numero1 - numero2}")
    else:
        print(f"{numero2} - {numero1} = {numero2 - numero1}")
elif opcao == 3:
    print(f"{numero1} x {numero2} = {numero1 * numero2}")
elif opcao == 4:
    if numero2 == 0:
        numero2 = int(input("Denominador não pode ser zero, digite outro valor: "))
    print (f"{numero1} / {numero2} = {numero1 / numero2}") 