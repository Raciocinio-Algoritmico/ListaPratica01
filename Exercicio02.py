from math import sqrt

numero = float(input("Digite um número real qualquer: "))

if numero >= 0:
    raiz = sqrt(numero)
    print(f"A raíz quadrada de {numero} é {raiz}")
else:
    print(f"{numero} ao quadrado é {pow(numero, 2)}")