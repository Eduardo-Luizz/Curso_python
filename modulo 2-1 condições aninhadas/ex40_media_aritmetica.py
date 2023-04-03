# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota do aluno(a): '))
nota2 = float(input('Digite a segunda nota do aluno(a): '))
media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Parabéns você foi APROVADO com média {media :.2f}')
elif media >= 6.9 or media >= 5:
    print(f'Poderia ter se esforçado mais, ficou em RECUPERAÇÃO média {media :.2f}')
else:
    print(f'Isso não deveria ter acontecido, reveja seus métodos, você foi REPROVADO com média {media :.2f}')
