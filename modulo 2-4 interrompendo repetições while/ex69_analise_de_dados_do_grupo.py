# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

somador_idades = somador_homens  = somador_mulheres = 0

while True:
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().lower()[0]
    if idade >= 18:
        somador_idades += 1
    if idade < 20 and sexo == 'f':
        somador_mulheres += 1
    if sexo == 'm':
        somador_homens += 1
    opcao = ' '
    while opcao not in 'sn':
        opcao = str(input('Deseja continuar ? [S/N]: ')).strip().lower()[0]
    if opcao == 'n':
        break

print(f'O total de pessoas com mais de 18 anos é {somador_idades}')
print(f'O total de homens é {somador_homens}')
print(f'O total de mulheres abaixo de 20 anos é {somador_mulheres}')
