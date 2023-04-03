# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_pares = []
lista_impares = []
contador = 0
while True:
    contador += 1
    valor = int(input(f'Digite o {contador} valor [0 - para sair]: '))
    if valor == 0:
        break
    lista.append(valor)
    if valor % 2 == 0:
        lista_pares.append(valor)
    else:
        lista_impares.append(valor)
print(f'A lista original é: {lista}')
print(f'A lista que contém somente os pares ficou: {lista_pares}')
print(f'A lista que contém somente os ímpares ficou: {lista_impares}')
