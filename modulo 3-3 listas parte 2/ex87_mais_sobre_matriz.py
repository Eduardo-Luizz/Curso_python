#  Aprimore o desafio anterior, mostrando no final:
#  A) A soma de todos os valores pares digitados.
#  B) A soma dos valores da terceira coluna.
#  C) O maior valor da segunda linha.
soma_pares = soma_terceira_coluna = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    soma_terceira_coluna += matriz[linha][2]
    print()
print(f'Soma dos pares: {soma_pares}')
print(f'Soma dos valores da terceira coluna: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
