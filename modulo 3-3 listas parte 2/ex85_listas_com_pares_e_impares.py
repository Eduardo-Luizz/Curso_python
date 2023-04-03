# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
lista = []
aux = []
aux2 = []
contador = 0
while contador <= 6:
    contador += 1
    number = (int(input(f'Digite o {contador} número: ')))
    if number % 2 == 0:
        aux.append(number)
    else:
        aux2.append(number)

aux.sort()
aux2.sort()
lista.append(aux[:])
lista.append(aux2[:])
aux.clear()
aux2.clear()
print(f'Lista copiada {lista}')
print(f'os valores pares {lista[0][0:]}')
print(f'os valores ímpares {lista[1][0:]}')