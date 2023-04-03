# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

GREEN = "\033[0;32m"
RED = "\033[1;31m"
RESET = "\033[0;0m"

resultado = 0
vitorias_consecutivas = 0
while True:
    jogada_do_computador = randint(0, 10)
    jogada_do_usuario = int(input('\nDigite um número: '))
    opcao_usuario = str(input('Você quer PAR ou ÍMPAR: [P\I]: ')).strip().lower()
    resultado = jogada_do_computador + jogada_do_usuario

    if opcao_usuario == 'p' and resultado % 2 == 0:
        vitorias_consecutivas += 1
        print(f'\nVocê escolheu {opcao_usuario}')
        print(f'Você jogou {jogada_do_usuario}')
        print(f'Computador jogou {jogada_do_computador}')
        print(f'Resultado = {resultado}')
        print(GREEN + 'Parabéns você ganhou' + RESET)
    elif opcao_usuario == 'i' and resultado % 2 != 0:
        vitorias_consecutivas += 1
        print(f'\nVocê escolheu {opcao_usuario}')
        print(f'Você jogou {jogada_do_usuario}')
        print(f'Computador jogou {jogada_do_computador}')
        print(f'Resultado = {resultado}')
        print(GREEN + 'Parabéns você ganhou' + RESET)
    else:
        print(f'\nVocê escolheu {opcao_usuario}')
        print(f'Você jogou {jogada_do_usuario}')
        print(f'Computador jogou {jogada_do_computador}')
        print(f'Resultado = {resultado}')
        print(RED + 'Computador ganhou' + RESET)
        break
print(f'Você conseguiu uma sequência de {vitorias_consecutivas} vitórias')
