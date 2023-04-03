# Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digtite a razão da P.A: '))
n = 10

decimo_termo = primeiro_termo + (n - 1) * razao
decimo_termo += 1

for c in range(primeiro_termo, decimo_termo, razao):
    print(f'{c} ->', end=' ')
print('Acabou')
