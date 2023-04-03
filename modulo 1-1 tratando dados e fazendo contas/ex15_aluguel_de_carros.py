#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

totalPercorrido = float(input('Digite o total de Km: '))
totalDias = int(input('Digite o total de dias em que o carro ficou locado: '))
valorTotalPagoPorDia = totalDias * 60
valorTotalPagoPorKm = totalPercorrido * 0.15
soma = valorTotalPagoPorDia + valorTotalPagoPorKm

print(f'O carro andou {totalPercorrido}Km \nPermaneceu em uso por {totalDias} dias\nVocê deve pagar R${soma :.2f}')
