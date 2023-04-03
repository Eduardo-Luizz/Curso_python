# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

lista = []
for c in range(1, 6):
    peso = float(input(f'Digite o pesso da {c}º pessoa: '))
    lista.append(peso)

print(f'O maior peso foi: {max(lista):.2f}Kg')
print(f'O menor peso foi: {min(lista):.2f}Kg')


maior = 0
menor = 0
for p in range(1, 6):
    pesoTotal = float(input('Digite o peso: '))
    if p == 1:
        menor = pesoTotal
        maior = pesoTotal
    else:
        if pesoTotal > maior:
            maior = pesoTotal
        if pesoTotal < menor:
            menor = pesoTotal
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')