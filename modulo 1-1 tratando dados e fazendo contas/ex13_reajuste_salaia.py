# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite um salário: R$'))

porcentagem = (salario * 15) / 100
valorFinal = salario + porcentagem

print(f'O salário era {salario} \nCom 15% de aumento ficou {valorFinal :.2f}')
