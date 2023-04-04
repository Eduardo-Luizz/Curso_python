import Aula_22_uteis_modulo
from Uteis_package import numeros

num = int(input('Digite um valor: '))
fat = Aula_22_uteis_modulo.fatorial(num)
dob = numeros.dobro(num)

print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dob}')
