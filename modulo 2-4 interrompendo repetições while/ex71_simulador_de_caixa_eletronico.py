# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('Quanto você deseja sacar: R$'))
total = valor
cedula_inicial = 50
total_de_cedulas = 0
while True:
    if total >= cedula_inicial:
        total -= cedula_inicial
        total_de_cedulas += 1
    else:
        if total_de_cedulas > 0:
            print(f'Total de {total_de_cedulas} cédulas de R${cedula_inicial}')
        if cedula_inicial == 50:
            cedula_inicial = 20
        elif cedula_inicial == 20:
            cedula_inicial = 10
        elif cedula_inicial == 10:
            cedula_inicial = 1
        total_de_cedulas = 0
        if total == 0:
            break
print('Operação finalizada')
