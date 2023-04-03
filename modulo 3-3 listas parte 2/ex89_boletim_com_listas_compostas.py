# Crie um programa que
# leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = []
id = 0
media = 0
while True:
    name = str(input('Digite o nome do aluno (ou "sair" para encerrar): ')).strip()
    if name.lower() == 'sair':
        break
    note1 = float(input('Digite a primeira nota: '))
    note2 = float(input('Digite a segunda nota: '))
    lista.append([id, name, note1, note2])
    id += 1

for aluno in lista:
    media = (aluno[2] + aluno[3]) / 2
    print("{:^10}\t{:^10}\t{:^10}".format(aluno[0], aluno[1], media))

while True:
    escolha = int(input('Digite o Id de qual aluno deseja visualizar as notas (ou "999" para encerrar): '))
    if escolha == 999:
        break
    for aluno in lista:
        if aluno[0] == escolha:
            print(f'Id: {aluno[0]} Nome: {aluno[1]} Notas: {aluno[2]} {aluno[3]}')
            break
    else:
        print('Aluno não encontrado')
