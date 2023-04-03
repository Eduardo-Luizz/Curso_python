#  Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

dic = {}
lista_de_dados = []
lista_de_gols = []
id = 0

while True:
    id += 1
    dic['Cod'] = id
    nome = str(input('Nome do jogador: ')).strip().lower()
    total_de_partidas = int(input(f'Quantas partidas {nome} jogou: '))
    for gols in range(1, total_de_partidas + 1):
        total_de_gols_por_partida = int(input(f'Total de gols na {gols} partida: '))

        lista_de_gols.append(total_de_gols_por_partida)

    dic['Nome'] = nome
    dic['Gols'] = lista_de_gols[:]
    dic['Total'] = sum(lista_de_gols)
    lista_de_gols.clear()
    lista_de_dados.append(dic.copy())

    option = ' '
    while option not in 'sn':
        option = str(input('Deseja continuar [S/N]: ')).strip().lower()[0]
        if option not in 'sn':
            print('Deve ser digitado S/N !!!')
    if option in 'n':
        break
print('-=' * 30)
print('cod:\tnome:\tgols:\ttotal:')
for e in lista_de_dados:
    for chave, valor in e.items():
        print(f'\t{valor}', end=' ')
    print()
print('-=' * 30)
while True:
    dados_jogador = int(input('Mostrar os dados de qual jogador (999 para parar): '))
    if dados_jogador == 999:
        break
    else:
        jogador = lista_de_dados[dados_jogador - 1]
        gols_por_partida = jogador['Gols']
        for index, gols in enumerate(gols_por_partida):
            print(f'No jogo {index + 1} fez {gols} gols.')
