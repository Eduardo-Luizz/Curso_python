#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

money = float(input('Quanto dinheiro você tem na carteira: R$'))

print(f'Com R${money :.2f} você pode comprar U${money / 5.22 :.2f}')
