# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('palmeiras', 'internacional', 'fluminense', 'corinthians', 'flamengo', 'athletico-pr', 'atletico-mg',
         'fortaleza', 'são paulo', 'america-mg', 'botafogo', 'santos', 'goias', 'red bull bragantino', 'coritiba',
         'cuiaba', 'ceara', 'atletico-go', 'avai', 'juventude')

print(f'Lista de times do Brasileirão: {times}')
print(f'Os cinco primeiros times foram: {times[:6]}')
print(f'Os últimos 4 colocados foram: {times[-4:]}')
print(f'Ordenação por ordem alfabética: {sorted(times)}')
print(f"O Internacional está na posição: {times.index('internacional') + 1}")
