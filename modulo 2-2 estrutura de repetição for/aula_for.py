# Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, que é uma estrutura versátil e simples de entender. Por exemplo:
for c in range(0, 4):
    print(c)
print('Acabou')

for c in range(1, 6):
    print('Oi')
print('FIM')

for c in range(6, 0, -1):
    print(c)
print('fim')

n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)
print('FFF')

#PASSOS
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c)
print('Fte')

#SOMATÓRIO
a = 0
for c in range(0, 5):
    n = int(input(f'Digite o {c} número: '))
    a += n
print(f'Acabou {a}')
