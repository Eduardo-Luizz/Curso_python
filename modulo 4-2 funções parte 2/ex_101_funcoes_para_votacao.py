# Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano_nascimento):
    from datetime import datetime
    anos = datetime.now().year - ano_nascimento
    if anos < 16:
        return f'Com {anos} anos: NÃO VOTA'
    elif 18 <= anos < 70:
        return f'Com {anos} anos: VOTO É OBRIGATÓRIO'
    else:
        return f'Com {anos} anos: VOTO É OPCIONAL'


year = int(input('Em que ano você nasceu: '))

print(voto(year))
