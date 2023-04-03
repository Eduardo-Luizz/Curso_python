# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))

if number1 > number2:
    print(f'\nOs números digitados foram {number1} e {number2} \nO primeiro número digitado é maior com valor {number1}')
elif number2 > number1:
    print(f'\nOs números digitados foram {number1} e {number2} \nO segundo número digitado é maior com valor {number2}')
else:
    print(f'\nOs números digitados foram {number1} e {number2} \nE são iguais')
