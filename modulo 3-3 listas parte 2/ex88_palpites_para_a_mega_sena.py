# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

print('-' * 50)
print(f'{"JOGA NA MEGA":^5}')
print('-' * 50)

numeros = []
aux = []
contador = 0

total_jogadas = int(input('Quantas jogadas vc deseja: '))
while not total_jogadas == 0:
    total_jogadas -= 1
    for c in range(0, 6):
        aux.append(randint(0, 60))
    numeros.append(aux[:])
    aux.clear()

for linha in numeros:
    contador += 1
    print(f'Jogo {contador} :', end=' ')
    for elemento in linha:
        print(f'[{elemento:^4}]', end='')
    print()
