# Desenvolva um programa que
# leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.

acumulador_de_idades = 0
maior_idade = 0
contador_menos_de_20 = 0
nome_homem_mais_velho = ''
for pessoa in range(1, 5):
    nome = str(input(f'\nDigite o nome da {pessoa}º pessoa: ')).strip()
    idade = int(input(f'Digite a idade da {pessoa}º pessoa: '))
    sexo = str(input(f'Digite o sexo da {pessoa}º pessoa \n[ F ] Feminino - [ M ] Masculino - [ O ] - Outro: ')).strip().upper()
    acumulador_de_idades += idade
    media_de_idades = acumulador_de_idades / 4
    if pessoa == 1:
        maior_idade = idade
        nome_homem_mais_velho = nome
    else:
        if idade > maior_idade and sexo == 'M':
            maior_idade = idade
            nome_homem_mais_velho = nome
    if sexo == 'F':
        if idade < 20:
            contador_menos_de_20 += 1

print(f'\nA média das idades digitadas foi {media_de_idades}')
print(f'A maior idade foi {maior_idade} do homem chamado {nome_homem_mais_velho}')
print(f'A quantidade de mulheres com menos de 20 anos é {contador_menos_de_20}')
