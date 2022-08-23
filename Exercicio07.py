numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))

if numero1 > numero3:
    numero1, numero3 = numero3, numero1

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

if numero2 > numero3:
    numero2, numero3 = numero3, numero2

print(f"A ordem crescente dos números é: {numero1}, {numero2}, {numero3}")