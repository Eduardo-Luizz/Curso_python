# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter

dicionario = {}
ranking = []

for c in range(1, 5):
    dicionario[f"Jogador{c}"] = randint(1, 6)

print('Valores sorteados:')
for key, value in dicionario.items():
    print(f'- {key} tirou {value} no dado')
ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True) # itemgetter(1) está pegando o valor do radint se passar 0 no lugar de 1 pega o valor do jogador
print('=-' * 30)
print('RANKING: ')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
