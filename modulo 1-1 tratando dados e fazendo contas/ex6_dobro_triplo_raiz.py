#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math

number1 = int(input('Digite um número: '))
raiz = math.sqrt(number1)
print(f'O número digitado foi: {number1} \n Seu dobro é {number1 * 2} \n Seu triplo é {number1 * 3} \n A raiz quadrada é {raiz :.2f}')
