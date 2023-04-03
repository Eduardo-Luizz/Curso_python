# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa,
# o salário do comprador
# e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

house_value = float(input('Digite o valor da casa: '))
salary = float(input('Digite o salário do comprador: '))
years = float(input('Digite em quantos anos deseja pagar: '))
percentage = (salary * 30) / 100
prestacao = house_value / (years * 12)

if percentage > prestacao:
    print(f'Empréstimo concedido \n30% do salário {percentage :.2f} \nprestação mensal {prestacao :.2f}')
else:
    print(f'Empréstimo negado \nA prestação mensal ficou {prestacao :.2f} \nLogo excedeu 30% do seu salário que é {percentage :.2f}')
