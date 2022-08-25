numero = int(input("Digite um número inteiro qualquer: "))

if numero % 3 == 0 or numero % 5 == 0:
    if not(numero % 3 == 0 and numero % 5 == 0):
        print("Número divisível por 3 ou por 5, mas não por ambos")