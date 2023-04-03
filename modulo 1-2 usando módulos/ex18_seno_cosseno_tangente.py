#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo desejado: '))
rad = radians(angulo)

print(f'O ângulo de {angulo} tem o SENO de {sin(rad) :.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cos(rad) :.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {tan(rad) :.2f}')
