# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

aproveitamento = {}
cont = 0
list = []

name = str(input('Nome: ')).strip()
amount = int(input('Partidas: '))

for gols in range(1, amount + 1):
    amount_goals = int(input(f'Total de gols na {gols} partida: '))
    cont += amount_goals
    list.append(amount_goals)

aproveitamento['Nome'] = name
aproveitamento['Total_de_partidas'] = list
aproveitamento['Total_de_gols'] = cont
print('-=' * 30)
print(aproveitamento)
print('-=' * 30)
for key, value in aproveitamento.items():
    print(f'O campo {key} tem valor {value}')
print('-=' * 30)
print(f'O jogador {name} jogou {amount} partidas.')
for index, elemento in enumerate(list):
    print(f'=> Na partida {index}, fez {elemento} gols.')
print(f'Foi um total de {cont} gols')
