# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    print('-=' * 30)
    print(f'Analisando os valores passados...')
    for c in num:
        print(f'{c}', end=' ')
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {max(num)}')
    print('-=' * 30)


maior(1, 2, 3)
maior(10, 20, 1000)
maior(0)
