# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total_gasto = preco_acima_de_mil = 0
nome_mais_barato = ''
preco_produtos = []

print('-' * 30)
print('       LOJA DO DESCONTO')
print('-' * 30)

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$'))
    total_gasto += preco
    preco_produtos.append(preco)
    if preco > 1000:
        preco_acima_de_mil += 1
    if min(preco_produtos):
        nome_mais_barato = nome
    opcao = ' '
    while opcao not in 'sn':
        opcao = str(input('Deseja continuar ? [S/N]')).strip().lower()[0]
    if opcao == 'n':
        break
print(f'\nO total gasto foi de: {total_gasto :.2f}')
print(f'O total de produtos acima de mil reais é: {preco_acima_de_mil}')
print(f'O nome do produto mais barato é: {nome_mais_barato} custando R${min(preco_produtos) :.2f}')
