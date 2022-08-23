altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

if peso < 60:
    if altura < 1.20:
        print("A")
    elif altura >= 1.20 and altura <= 1.70:
        print("B")
    else:
        print("C")
elif peso >= 60 and peso <= 90:
    if altura < 1.20:
        print("D")
    elif altura >= 1.20 and altura <= 1.70:
        print("E")
    else:
        print("F")
else:
    if altura < 1.20:
        print("G")
    elif altura >= 1.20 and altura <= 1.70:
        print("H")
    else:
        print("I")