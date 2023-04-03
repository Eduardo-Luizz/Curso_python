# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

somador = 0
contador = 0
for c in range(1, 7):
    number = int(input(f'Digite o {c}º número: '))

    if number % 2 == 0:
        somador += number
        contador += 1
print(f'Foram {contador} números somados \nObtendo a soma {somador}')
