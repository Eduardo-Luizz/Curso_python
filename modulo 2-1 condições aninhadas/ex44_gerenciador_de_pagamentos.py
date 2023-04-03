# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

value = float(input('Digite o valor a ser pago: '))
print(
'''\nNossos métodos de pagamento disponíveis:
[ 1 ] À vista
[ 2 ] À vista no cartão
[ 3 ] Em 2x no cartão
[ 4 ] Em 3x ou mais no cartão
''')
method_payment = int(input('Digite o método de pagamento: '))

percentage_value = 0
division = 100

if method_payment == 1:
    percentage_value = 10
    percentage = (value * percentage_value) / division
    total_value = value - percentage
    print(f'À vista \nDireito a 10% de desconto \nTotal a pagar: R${total_value :.2f}')

elif method_payment == 2:
    percentage_value = 5
    percentage = (value * percentage_value) / division
    total_value = value - percentage
    print(f'À vista no cartão \nDireito a 5% de desconto \nTotal a pagar: R${total_value :.2f}')

elif method_payment == 3:
    plots = value / 2
    print(f'Em 2x no cartão \nPreço normal \nValor por parcela: R${plots :.2f} \nTotal a pagar: R${value :.2f}')

elif method_payment == 4:
    percentage_value = 20
    percentage = (value * percentage_value) / division
    total_value = value + percentage
    quantity_plots = int(input('Digite quantas parcelas você deseja: '))
    plots = total_value / quantity_plots
    print(f'Em 3x ou mais no cartão \nAumento de 20% \nValor por parcela: R${plots :.2f} \nTotal a pagar: R${total_value :.2f}')
else:
    print('opção inválida !!!')
