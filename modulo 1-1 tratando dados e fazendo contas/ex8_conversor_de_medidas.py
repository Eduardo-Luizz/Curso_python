#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Digite o valor desejado: m '))

print(f'O valor digitado foi {metros} \nConvertido para cm é {metros * 100 :.0f} \nConvertido para mm é {metros * 1000 :.0f}')
