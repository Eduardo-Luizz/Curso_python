# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

tupla = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')))

print(f'Lista de números: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'A primeira posição que o valor 3 apareceu foi: {tupla.index(3) + 1}')
else:
    print('O valor 3 não foi digitado')
print('Os números que são pares: ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
