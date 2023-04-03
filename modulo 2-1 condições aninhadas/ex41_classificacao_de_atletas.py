# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import date

year_of_birth = int(input('Digite o ano de nascimento do atleta: '))
age_now = date.today().year - year_of_birth

if age_now > 25:
    print(f'MASTER com {age_now} anos')
elif age_now <= 25 and age_now > 19:
    print(f'SÊNIOR com {age_now} anos')
elif age_now <= 19 and age_now > 14:
    print(f'JÚNIOR com {age_now} anos')
elif age_now <= 14 and age_now > 9:
    print(f'INFATIL com {age_now} anos')
else:
    print(f'MIRIM com {age_now} anos')
