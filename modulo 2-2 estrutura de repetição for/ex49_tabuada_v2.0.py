# Refaça o DESAFIO 9,
# mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

number = int(input('Digite o número que deseja obter a tabuada: '))
for c in range(0, 11):
    print(f'{number} X {c} = {number * c}')
