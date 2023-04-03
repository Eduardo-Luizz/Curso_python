# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase_list = str(input('Digite a frase: ')).strip().upper().replace(' ', '')
for index in range(len(frase_list)):
    frase_invertida = frase_list[::-1].replace(' ', '')
if frase_list == frase_invertida:
    print(f'\nA frase digitada foi {frase_list}, O inverso dela ficou {frase_invertida}')
    print('É um palindromo')
else:
    print(f'\nA frase digitada foi {frase_list}, O inverso dela ficou {frase_invertida}')
    print('Não é um palindromo')
