# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

contador = resultado = 0
while True:
    numero = int(input('Digite o número que deseja obter a tabuada: '))
    if numero < 0:
        break
    while contador <= 10:
        print(f'{numero} X {contador} = {resultado}')
        contador += 1
        resultado = numero * contador
    contador = 0
    resultado = 0
print('Programa da tabuada encerrado, tenha um bom dia!')
