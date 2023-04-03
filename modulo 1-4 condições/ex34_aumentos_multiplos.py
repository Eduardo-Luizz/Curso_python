# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

money = float(input('Digite seu salário: '))

if money <= 1250:
    porcentagem = (money * 15) / 100
    valorFinal = money + porcentagem
    print(f'O seu salário era {money} \nO reajuste de 15% ficou {porcentagem} \nO valor final é {valorFinal}')
elif money > 1250:
    porcentagem = (money * 10) / 100
    valorFinal = money + porcentagem
    print(f'O seu salário era {money} \nO reajuste de 10% ficou {porcentagem} \nO valor final é {valorFinal}')
