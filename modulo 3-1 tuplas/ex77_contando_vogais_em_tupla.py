# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ('APRENDER', 'PROGRAMAR', 'LNGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
         'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for valor in tupla:
    print(f'\nNa palavra {valor} temos', end=' ')
    for letra in valor:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')