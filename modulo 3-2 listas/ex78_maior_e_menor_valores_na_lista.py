# Faça um programa que leia 5 valores numéricos e
# guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
for contador in range(0, 5):
    lista.append(int(input(f'Digite o {contador}º valor: ')))
print(lista)
print(f'O maior valor da lista foi {max(lista)} nas posições ', end='')
for index, valor in enumerate(lista):
    if valor == max(lista):
        print(f'{index}...', end='')
print()
print(f'O menor valor da lista foi {min(lista)} nas posições ', end='')
for index, valor in enumerate(lista):
    if valor == min(lista):
        print(f'{index}...', end='')
print()