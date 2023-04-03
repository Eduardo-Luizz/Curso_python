# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continuar = 's'
contador = somador = 0

lista = []

while continuar != 'n':
    numero = int(input('Digite um número: '))
    continuar = str(input('Você deseja continuar ? [S/N]: ')).strip().lower()
    somador += numero
    contador += 1
    lista.append(numero)

media = somador / contador
print(f'Você digitou {contador} números e a média atitmética é {media :.2f}')
print(f'O maior valor da lista foi {max(lista)} e o menor valor foi {min(lista)}')
