# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

contador = 0
lista = []
repeticoes = []
while True:
    contador += 1
    valor = int(input(f'Digite o {contador}º valor [0 - para sair]: '))
    if valor == 0:
        break
    if valor not in lista:
        lista.append(valor)
lista.sort()
print(f'A lista sem valores repitods ficou {lista}')
