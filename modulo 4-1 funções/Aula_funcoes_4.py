# Empacotar parametros

def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('Fim')
    print(f'Recebi os valores {num} e são ao todo {len(num)} números')

contador(2, 1, 7)
contador(8)
contador(4, 3, 2, 1, 0)
