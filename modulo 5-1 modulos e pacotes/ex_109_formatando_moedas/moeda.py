def aumentar(valor, taxa, formato = False):
    resultado = valor + (valor * taxa / 100)
    return formatar_moeda(resultado) if formato else resultado

def diminuir(valor, taxa, formato = False):
    resultado = valor - (valor * taxa / 100)
    return formatar_moeda(resultado) if formato else resultado

def dobro(valor, formato = False):
    resultado = valor * 2
    return formatar_moeda(resultado) if formato else resultado

def metade(valor, formato = False):
    resultado = valor / 2
    return formatar_moeda(resultado) if formato else resultado

def formatar_moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')

def moeda(preco, taxa):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{formatar_moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, False)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa}% de aumento: \t{aumentar(preco, taxa, True)}')
    print(f'{taxa}% de redução: \t{diminuir(preco, taxa, True)}')
    print('-' * 30)