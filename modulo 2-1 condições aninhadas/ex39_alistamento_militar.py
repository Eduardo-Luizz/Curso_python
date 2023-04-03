#Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar
# ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta
# ou que passou do prazo.

from datetime import date

name = str(input('Digite o nome da pessoa: '))
year = int(input('Digite o ano de nascimento da pessoa: '))
age_now = date.today().year - year
time = age_now - 18
convert_num = str(time)
if age_now == 18:
    print(f'Olá Sr(a) {name} \nVocê tem {age_now} anos \nESTÁ É A HORA EXATA PARA SE ALISTAR')
elif age_now > 18:
    print(f'Olá Sr(a) {name} \nVocê tem {age_now} anos \nJÁ PASSOU EM {time} ANOS, DA IDADE DE ALISTAMENTO, REGULARIZE SEU DEVER URGENTEMENTE!!!')
elif age_now < 18:
    print(f'Olá Sr(a) {name} \nVocê tem {age_now} anos \nAINDA FALTAM {convert_num[1:]} ANOS, NÃO ESTÁ NA IDADE PARA FAZER ALISTAMENTO, AGUARDE ...')
