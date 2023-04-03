# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados
# e qual foi a soma entre elas (desconsiderando o flag).

total_de_numeros_digitados = soma_dos_numeros_digitados = 0
while True:
    numero = int(input('Digite um número: [999 para parar]: '))
    if numero == 999:
        break
    total_de_numeros_digitados += 1
    soma_dos_numeros_digitados += numero

print(f'O total de números digitados foi {total_de_numeros_digitados}\nE a soma total dos números digitados é {soma_dos_numeros_digitados}')
