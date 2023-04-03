# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

total_maiores_de_idade = 0
total_menores_de_idade = 0
for c in range(1, 7):
    years = int(input(f'Digite o ano de nascimento da {c}º pessoa: '))
    age_now = date.today().year - years
    if age_now >= 18:
        total_maiores_de_idade += 1
    else:
        total_menores_de_idade += 1

print(f'Total de pessoal que são de maiores {total_maiores_de_idade}')
print(f'Total de pessoal que são de menores {total_menores_de_idade}')

