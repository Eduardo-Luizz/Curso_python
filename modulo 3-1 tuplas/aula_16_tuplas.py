lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

for contador in range(0, len(lanche)):
    print(f'Eu comi {contador}')
    print(f'Lanche {lanche[contador]}')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba')

#ordenar
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
# total de números dentro da tupla
print(len(c))
# total de vezes que 5 aparece
print(c.count(5))
# em qual posição está o 8
print(f'Em qual posição está {c.index(8)}')
print(f'Pegando sem ser a primeira ocorrência {c.index(5, 1)}')

