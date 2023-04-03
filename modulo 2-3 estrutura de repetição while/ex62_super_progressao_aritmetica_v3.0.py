# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digtite a razão da P.A: '))
termo = primeiro_termo
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} ->', end=' ')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais ? '))
print(f'Progressão finalizada com {total} termos mostrados')
