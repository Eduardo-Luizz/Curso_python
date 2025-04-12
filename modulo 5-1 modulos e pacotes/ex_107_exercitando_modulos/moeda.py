# Crie um módulo chamado moeda.py
# que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(valor, taxa):
    resultado = valor + (valor * taxa / 100)
    return print(f'Aumentando {taxa}%, temos R${resultado}')

def diminuir(valor, taxa):
    resultado = valor - (valor * taxa / 100)
    return print(f'Diminuindo {taxa}%, temos R${resultado}')

def dobro(valor):
    return print(f'O dobro de R${valor} é R${valor * 2}')

def metade(valor):
    return print(f'A metade de R${valor} é R${valor / 2}')