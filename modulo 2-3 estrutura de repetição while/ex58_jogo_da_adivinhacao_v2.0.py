# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computer_choice = randint(0, 10)

BLUE = "\033[1;34m"
GREEN = "\033[0;32m"
RED = "\033[1;31m"
RESET = "\033[0;0m"

print(BLUE + "=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=")
print(GREEN + "Vou pensar em um número entre 0 e 5. Tente adivinhar ...")
print(BLUE + "=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=")

choice = 20
attempts = 1
acertou = False
while not acertou:
    choice = int(input(RESET + 'Qual é seu palpite: '))
    if computer_choice > choice:
        print('Mais... Tente mais uma vez')
        attempts += 1
    elif computer_choice < choice:
        print('Menos... Tente novamente')
        attempts += 1
    else:
        print(GREEN + f'Acertou com {attempts} tentativas')
