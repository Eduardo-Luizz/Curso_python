# Desenvolva uma lógica que leia
# o peso
# e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
if imc > 40:
    print(f'\nOBESIDADE MÓRBIDA \nCom {imc :.2f} \nValores de referência: Acima de 40')
elif imc <= 40 and imc > 30:
    print(f'\nOBESIDADE \nCom {imc :.2f} \nValores de referência: De 40 até 30')
elif imc <= 30 and imc > 25:
    print(f'\nSOBREPESO \nCom {imc :.2f} \nValores de referência: De 30 até 25')
elif imc <= 25 and imc > 18.5:
    print(f'\nPeso ideal \nCom {imc :.2f} \nValores de referência: De 25 até 18.5')
else:
    print(f'\nAbaixo do peso \nCom {imc :.2f} \nValores de referência: Abaixo de 18.5')