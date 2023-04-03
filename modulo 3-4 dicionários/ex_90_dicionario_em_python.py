# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
obj = {}


obj['nome'] = name = str(input('Nome: '))
obj['media'] = float(input(f'Média de {name}: '))
if obj['media'] < 5:
    obj['status'] = 'Reprovado'
elif obj['media'] >= 5 and obj['media'] < 7:
    obj['status'] = 'Em exame'
else:
    obj['status'] = 'Aprovado'

for key, value in obj.items():
    print(f' - {key} = {value}')