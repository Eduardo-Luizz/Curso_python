# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

number = int(input('Digite um número decimal para a conversão: '))
print('''\nAtendemos as seguintes opções :
[ 1 ] - Binário
[ 2 ] - Octal
[ 3 ] - Hexadecimal
''')
option = int(input('Digite uma opção: '))
if option == 1:
    bin_convert = bin(number)
    print(f'O número em decimal digitado foi {number} \nE convertido em binário é {bin_convert[2:]}')
elif option == 2:
    oct_convert = oct(number)
    print(f'O número em decimal digitado foi {number} \nE convertido em octal é {oct_convert[2:]}')
elif option == 3:
    hex_convert = hex(number)
    print(f'O número em decimal digitado foi {number} \nE convertido em hexadecimal é {hex_convert[2:]}')
else:
    print('Desculpe, opção não é válida !!!')
