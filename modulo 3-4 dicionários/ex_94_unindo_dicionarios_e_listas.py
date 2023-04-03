# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
pessoas = {}
lista_de_pessoas = []
lista_de_mulheres = []
total_de_cadastros = 0
total_de_idades = 0
while True:
    total_de_cadastros += 1
    pessoas['nome'] = str(input('Nome: ')).strip()
    pessoas['sexo'] = ' '
    while pessoas['sexo'] not in 'mMfF':
        pessoas['sexo'] = str(input('Sexo: ')).strip().lower()[0]
    pessoas['idade'] = int(input('Idade: '))
    total_de_idades += pessoas['idade']
    lista_de_pessoas.append(pessoas.copy())
    if pessoas['sexo'] == 'f':
        lista_de_mulheres.append(pessoas['nome'])
    option = ' '
    while option not in 'sSnN':
        option = str(input('Deseja continuar [S/N]: ')).strip().lower()[0]
    if option in 'n':
        break

print('-=' * 30)
print(f'A) Ao todo foram {total_de_cadastros} pessoas cadastradas')
print(f'B) A média das idades é de {total_de_idades / total_de_cadastros :.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end=' ')
for mulheres in lista_de_mulheres:
    print(mulheres, end=' ')
