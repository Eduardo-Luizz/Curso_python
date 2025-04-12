def leiaDinheiro(text):

    while True:
        valor_digitado = str(input(text)).replace(',', '.').strip()
        
        if valor_digitado.isalpha() or valor_digitado == '':
            print(f'\033[31mErro: "{valor_digitado}" é um preço inválido!\033[m')

        else:
            return float(valor_digitado)
