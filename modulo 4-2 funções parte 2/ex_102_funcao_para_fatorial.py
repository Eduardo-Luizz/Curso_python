# Crie um programa que tenha uma função fatorial()
# que receba dois parâmetros:
# o primeiro que indique o número a calcular
# e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=True):
    """
    -> Calcula o fatorial de um número.
    :param num: Número a ser calculado o fatorial
    :param show: (Opcional) se será mostrada ou não a operação
    :return: Retorna o valor do fatorial do número
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
    return f


print(fatorial(5, False))

print(help(fatorial))
