# Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)

RED = "\033[1;31m"
RESET = "\033[0;0m"


def leiaInt(valor):
    while True:
            n = input(valor)
            if n.isnumeric():
                return int(n)
            print(RED + 'ERRO! digite um número inteiro válido.')


n = leiaInt(RESET + 'Digite um número: ')
print(f'Você digitou {n}')
