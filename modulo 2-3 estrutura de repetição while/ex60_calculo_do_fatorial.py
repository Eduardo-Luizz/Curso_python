# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

#number = int(input('Digite um número: '))
#contador = number
#while contador != 1:
#    contador -= 1
#    teste = number * contador
#    print(f'Contador : {contador}\n Multiplicação {teste}')

numero = int(input("Fatorial de: ") )

resultado = 1
count = 1

while count <= numero:
    resultado *= count
    count += 1
    print(count)

print(resultado)
