# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distance = float(input('Qual a distância da viagem: Km '))

if distance <= 200:
    print(f'Sua viagem foi de {distance :.0f}Km \nCustando R${distance * 0.50 :.2f}')
else:
    print(f'Sua viagem foi de {distance}Km \nCustando R${distance * 0.45 :.2f}')
