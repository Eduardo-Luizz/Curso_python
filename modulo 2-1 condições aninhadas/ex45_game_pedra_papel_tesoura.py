# Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint

print('''
Seja bem vindo ao GAME : )
Sou seu computador, e proponho um jogo chamdo JOKENPO
\nSuas opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
''')

computer_choice = randint(1, 3)

sleep(2)
print('Pense em sua jogada ...')
print('===== 5')
sleep(1)
print('==== 4')
sleep(1)
print('=== 3')
sleep(1)
print('== 2')
sleep(1)
print('= 1')
sleep(1)
choice = int(input('Qual sua jogada: '))
print('Jo')
sleep(2)
print('ken')
sleep(2)
print('po')

if computer_choice == choice:
    print('EMPATE \njogadas iguais')
elif computer_choice == 1 and choice == 2:
    print('Computador jogou PEDRA \nPlayer jogou PAPEL \nPlayer ganhou')
elif computer_choice == 1 and choice == 3:
    print('Computador jogou PEDRA \nPlayer jogou TESOURA \nComputador ganhou')
elif computer_choice == 2 and choice == 1:
    print('Computador jogou PAPEL \nPlayer jogou PEDRA \nComputador ganhou')
elif computer_choice == 2 and choice == 3:
    print('Computador jogou PAPEL \nPlayer jogou TESOURA \nPlayer ganhou')
elif computer_choice == 3 and choice == 1:
    print('Computador jogou TESOURA \nPlayer jogou PEDRA \nPlayer ganhou')
elif computer_choice == 3 and choice == 2:
    print('Computador jogou TESOURA \nPlayer jogou PAPEL \nPlayer ganhou')