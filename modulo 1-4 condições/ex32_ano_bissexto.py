# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date
year = int(input('0 - ano atual ou digite o ano: '))

if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'O ano digitado foi {year}\nÉ BISSEXTO')
else:
    print(f'O ano digitado foi {year}\nNÃO É BISSEXTO')
