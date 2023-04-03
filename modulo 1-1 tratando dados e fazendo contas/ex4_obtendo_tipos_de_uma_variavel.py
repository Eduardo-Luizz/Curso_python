# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

inputUser = input('Digite algo:' )
print('O tipo primitivo é: ', type(inputUser))
print('Só tem espaços: ', inputUser.isspace())
print('É um número: ', inputUser.isnumeric())
print('É alfabético: ', inputUser.isalpha())
print('É alfanumérico: ', inputUser.isalnum())
print('Está em maiúscula: ', inputUser.isupper())
print('Está em minúscula: ', inputUser.islower())
print('Está capitalizada: ', inputUser.istitle())
