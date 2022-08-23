ladoA = float(input("Digite o primeiro lado: "))
ladoB = float(input("Digite o segundo lado: "))
ladoC = float(input("Digite o terceiro lado: "))

somaAB = ladoA + ladoB
somaBC = ladoB + ladoC
somaAC = ladoA + ladoC

if somaAB < ladoC or somaBC < ladoA or somaAC < ladoB:
    print("Não é um triângulo.")
elif ladoA == ladoB and ladoA == ladoC:
    print("Triângulo equilátero.")
elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
    print("Triângulo isóceles.")
else:
    print("Triângulo escaleno.")
    