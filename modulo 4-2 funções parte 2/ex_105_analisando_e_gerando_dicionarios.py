# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário
# com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

dic = {}


def notas(*nota, situation=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias)
    :param situation: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    dic['total'] = len(nota)
    dic['maior_valor'] = max(nota)
    dic['menor_valor'] = min(nota)
    dic['média'] = sum(nota) / dic['total']
    if situation:
        if dic['média'] < 5:
            dic['situação'] = 'RUIM'
        elif 5 < dic['média'] < 7:
            dic['situação'] = 'RAZOÁVEL'
        else:
            dic['situação'] = 'BOM'
    return dic


resp = notas(5.5, 9.5, 10, 6.5, situation=True)
print(resp)
help(notas)
