#  Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas.
# Uma listagem com as pessoas mais pesadas.
# Uma listagem com as pessoas mais leves.

contador = 0
peoples = []
aux = []
maior = menor = 0
while True:
    contador += 1
    name = str(input(f'Digite o {contador}º nome: '))
    weight = int(input(f'Digite a {contador}º peso: '))
    aux.append(name)
    aux.append(weight)
    if len(peoples) == 0:
        maior = menor = aux[1]
    else:
        if aux[1] > maior:
            maior = aux[1]
        if aux[1] < menor:
            menor = aux[1]
    peoples.append(aux[:])
    aux.clear()
    option = ' '
    while option not in 'sn':
        option = str(input('Deseja continuar [S/N]: ')).strip().lower()[0]
    if option == 'n':
        break
print(f'O maior peso foi de {maior}', end=' ')
for pessoa in peoples:
    if pessoa[1] == maior:
        print(f'{pessoa[0]}', end=' ')
print()
print(f'O menor peso foi de {menor}', end=' ')
for pessoa in peoples:
    if pessoa[1] == menor:
        print(f'{pessoa[0]}', end=' ')
print()
print(f'O total de pessoas cadastradas foi de {contador}')
print(peoples)
