# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ('Zero','Um','Dois','Três','Quatro',
         'Cinco','Seis','Sete','Oito','Nove',
         'Dez','Onze','Doze','Treze','Catorze',
         'Quinze','Dezesseis','Dezessete','Dezoito','Dezenove', 'Vinte')

number = int(input('Digite um número: '))
for posicao, contador in enumerate(tupla):
    if number < 0 or number > 20:
        number = int(input('O número que você digitou não está no intervalo esperado !!!\nDigite novamente: '))
    if number == posicao:
        print(f'Você digitou {contador}')
