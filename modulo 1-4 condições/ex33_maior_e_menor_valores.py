# Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor.

number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))
number3 = int(input('Digite o terceiro número: '))
menor = number1
if number2 < number1 and number2 < number3:
    menor = number2
if number3 < number1 and number3 < number2:
    menor = number3

maior = number1
if number2 > number1 and number2 > number3:
    maior = number2
if number3 > number1 and number3 > number2:
    maior = number3
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
