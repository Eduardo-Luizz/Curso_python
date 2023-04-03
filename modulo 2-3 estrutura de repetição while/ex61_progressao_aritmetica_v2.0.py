# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digtite a razão da P.A: '))
termo = primeiro_termo
contador = 1

while contador <= 10:
    print(f'{termo} ->', end=' ')
    termo += 1
    contador += 1
print('Acabou')