num = [2, 5, 9, 1, 2, 2]

num[2] = 100
num.append(700)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
if 2 in num:
    num.remove(2)
else:
    print('Não achei')
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for valore in valores:
    print(f'{valore}...', end='')

for chave, valore in enumerate(valores):
    print(f'\nNa posição {chave} encontrei o valor {valore}...')

for con in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

a = [2, 3, 4, 7]
b = a # faz uma ligação logo qualquer coisa que for alterada em uma lista será alterada na outra
b = a[:] # recebe uma copia dos valores não ligação logo se mudar em uma não muda na outra
print(f'Lista a: {a}')
print(f'Lista b: {b}')

