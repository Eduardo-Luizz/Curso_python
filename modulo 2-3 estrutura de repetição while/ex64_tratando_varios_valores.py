#  Crie um programa que leia vários números inteiros pelo teclado.
#  O programa só vai parar quando o usuário digitar o valor 999,
#  que é a condição de parada.
#  No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

number = somador = contador = 0
while not number == 999:
    number = int(input('Digite um número [999 para sair]: '))
    if number != 999:
        somador += number
        contador += 1
print(f'Você digitou {contador} números \nE a soma de todos eles é {somador}')
