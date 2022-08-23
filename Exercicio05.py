trabalhoLaboratorio = float(input("Digite a nota do trabalho de laboratório: "))
avaliacaoSemestral = float(input("Digite a nota da avaliação semestral: "))
exameFinal = float(input("Digite a nota do exame final: "))

media = (trabalhoLaboratorio * 0.2) + (avaliacaoSemestral * 0.3) + (exameFinal * 0.5)

if media >= 0 and media <= 2.9:
    print("Aluno reprovado!")
elif media >= 3 and media <= 4.9:
    print("Aluno de recuperação!")
else:
    print("Aluno aprovado!")