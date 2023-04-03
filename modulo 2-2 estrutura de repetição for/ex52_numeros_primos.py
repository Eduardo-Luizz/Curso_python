# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

BLUE = "\033[1;34m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"

number = int(input('Digite um número: '))
contador_de_multiplos = 0
for c in range(1, number + 1):
    if (number % c == 0):
        print(f'Divisível por {c}')
        contador_de_multiplos += 1
if contador_de_multiplos == 2:
    print('É primo')
else:
    print('Não é primo')
