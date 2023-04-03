# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Digite a temperatura em Celsius: '))

conversao = (celsius * 1.8) + 32

print(f'A temperatura digitada foi {celsius}C que corresponde à {conversao}F')
