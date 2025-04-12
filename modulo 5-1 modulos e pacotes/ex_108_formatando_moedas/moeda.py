def aumentar(valor, taxa):
    resultado = valor + (valor * taxa / 100)
    return resultado

def diminuir(valor, taxa):
    resultado = valor - (valor * taxa / 100)
    return resultado

def dobro(valor):
    return valor * 2

def metade(valor):
    return valor / 2

def formatar_moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')

def moeda(preco, taxa):
    print(f"A metade de {formatar_moeda(preco)} é {formatar_moeda(metade(preco))}")
    print(f"O dobro de {formatar_moeda(preco)} é {formatar_moeda(dobro(preco))}")
    print(f"Aumentando {taxa}%, temos {formatar_moeda(aumentar(preco, taxa))}")
    print(f"Diminuindo {taxa}%, temos {formatar_moeda(diminuir(preco, taxa))}")