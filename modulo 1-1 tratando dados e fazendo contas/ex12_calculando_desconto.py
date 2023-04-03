#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: R$'))

porcentagem = (preco * 5) / 100
valorFinal = preco - porcentagem

print(f'O preço do produto é {preco} \nCom 5% de desconto fica {valorFinal :.2f}')
