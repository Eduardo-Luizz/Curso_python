# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

print("O cateto oposto é {} \nO cateto adjacente é {} \nA Hipotenusa do triangulo é {:.2f} ".format(ca, co, hypot(ca, co)))
