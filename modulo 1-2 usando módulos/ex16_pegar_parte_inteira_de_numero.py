# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
number1 = float(input('Digite um numero: '))

print('O valor digitado foi : {} \nRetirando a parte fracionária ficou {}'.format(number1, math.trunc(number1)))
