# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# Quantos números foram digitados.
# A lista de valores, ordenada de forma decrescente.
# Se o valor 5 foi digitado e está ou não na lista.

lista = []
contador = total = 0
while True:
    contador += 1
    valor = int(input(f'Digite o {contador} valor: [0 - para sair]'))
    if valor == 0:
        break
    lista.append(valor)
print(f'A lista original: {lista}')
print(f'O total de valores digitados foi: {len(lista)}')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente: {lista}')
if 5 in lista:
    print('Sim o valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
