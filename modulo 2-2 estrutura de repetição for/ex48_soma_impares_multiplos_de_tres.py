# Faça um programa que
# calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

somador = 0
contador = 0
for c in range(1, 501, 2):
    if(c % 3 == 0):
        print(c)
        contador += 1
        somador += c
print(f'Fim \nSoma {somador} \nTotal de números {contador}')
