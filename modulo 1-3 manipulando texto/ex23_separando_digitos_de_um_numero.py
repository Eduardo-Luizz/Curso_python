# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

number = str(input('Digite um número: ')).strip()

print(f'Unidade {number[3]}')
print(f'Dezena {number[2]}')
print(f'Centena {number[1]}')
print(f'Milhar {number[0]}')
