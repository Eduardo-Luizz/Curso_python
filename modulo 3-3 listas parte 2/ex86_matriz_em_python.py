# Crie um programa que declare uma matriz de dimensão 3×3
# e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]
for c in range(0, 3):
    number = int(input(f'Digite um valor para a linha 0 coluna {c} : '))
    matriz[0].append(number)

for c in range(0, 3):
    number = int(input(f'Digite um valor para a linha 1 coluna {c} : '))
    matriz[1].append(number)

for c in range(0, 3):
    number = int(input(f'Digite um valor para a linha 2 coluna {c} : '))
    matriz[2].append(number)

for linha in matriz:
    print(linha)
