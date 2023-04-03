# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

GREEN = "\033[0;32m"
RED = "\033[1;31m"
RESET = "\033[0;0m"
LIMIT = 80
velocity = int(input('Digite a velocidade atual do carro: '))

if velocity > LIMIT:
    amount = (velocity - LIMIT) * 7
    print(RED + '\nMULTADO' + f' Você ultrapssou o limite de 80Km/h \nPassando há {velocity}Km/h \nRecebeu uma multa no valor de R${amount :.2f}')
else:
    print(GREEN + 'OK' + f'\nVelocidade atual {velocity}Km/h \nLimite 80Km/h')
