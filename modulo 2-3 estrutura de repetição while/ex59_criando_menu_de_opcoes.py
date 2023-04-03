# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

value1 = float(input('\nDigite o primeiro valor: '))
value2 = float(input('Digite o segundo valor: '))

print(
'''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
''')

option_user = False

while not option_user == 5:
    option_user = int(input('\nQual opção desejada: '))

    if option_user == 1:
        result = value1 + value2
        print(f'Operação escolhidda foi Soma \nO resultado é {result :.2f}')
    elif option_user == 2:
        result = value1 * value2
        print(f'Operação escolhidda foi Multiplicação \nO resultado é {result :.2f}')
    elif option_user == 3:
        if value1 > value2:
            print(f'Números digitados {value1 :.2f} e {value2 :.2f} maior é {value1 :.2f}')
        elif value1 < value2:
            print(f'Números digitados {value1 :.2f} e {value2 :.2f} maior é {value2 :.2f}')
        else:
            print(f'Números digitados {value1 :.2f} e {value2 :.2f} Números são iguais')
    elif option_user == 4:
        value1 = float(input('Digite o novo primeiro valor: '))
        value2 = float(input('Digite o novo segundo valor: '))
    else:
        print('Opção inválida')