# Lê 5 valores inteiros e armazena em uma lista
valores = []
for i in range(5):
    valor = int(input(f'Digite o {i+1}º valor: '))
    valores.append(valor)

# Encontra o maior e o menor valor e suas respectivas posições na lista
maior_valor = max(valores)
menor_valor = min(valores)
posicao_maior = valores.index(maior_valor)
posicao_menor = valores.index(menor_valor)

# Exibe os resultados na tela
print(f'O maior valor digitado foi {maior_valor}, na posição {posicao_maior}')
print(f'O menor valor digitado foi {menor_valor}, na posição {posicao_menor}')
