#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from time import sleep
from random import randint

BLUE = "\033[1;34m"
GREEN = "\033[0;32m"
RED = "\033[1;31m"
RESET = "\033[0;0m"

computer_choice = randint(0, 5)

print(BLUE + "=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=")
print(GREEN + "Vou pensar em um número entre 0 e 5. Tente adivinhar ...")
print(BLUE + "=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=")
print(RESET + "Pense :")
sleep(1)
print(RESET + "Pense :-")
sleep(1)
print(RESET + "Pense :-)")
sleep(1)
choice = int(input('Digite o número escolhido : '))
result = computer_choice == choice
if computer_choice != choice:
    print(RED + '\nPERDEU :( \n' + RESET + f'Você digitou o número: {choice}\nO computador escolheu {computer_choice}')
else:
    print(GREEN + '\nVENCEU :) \n' + RESET + f'Você digitou o número: {choice}\nO computador escolheu {computer_choice}')
