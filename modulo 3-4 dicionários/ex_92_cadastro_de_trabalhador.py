# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

trabalhador = {}

trabalhador['nome'] = str(input('Nome: '))
nascimento = int(input('Ano nascimento: '))
trabalhador['ctps'] = int(input('CTPS: '))
idade = date.today().year - nascimento
trabalhador['idade'] = idade
if trabalhador['ctps'] != 0:
    trabalhador['ano_de_contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: '))
    trabalhador['aposentadoria_em'] = trabalhador['idade'] + ((trabalhador['ano_de_contratacao'] + 35) - date.today().year)

for key, value in trabalhador.items():
    print(f'- {key}: {value}')
