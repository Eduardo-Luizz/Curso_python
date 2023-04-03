c = 1
while c != 10:
    print(c)
    c += 1

print('Acabou')

number = 1
par = impar = 0
while number != 0:
    number= int(input('Digite um numero: '))
    if number != 0:
        if number % 2 ==0:
            par += 1
        else:
            impar += 1
print(f'Você digitou par {par} e {impar} impar')

resposta = 'S'
while resposta == 'S':
    number = int(input('Digite um numero: '))
    resposta = str(input('Digite a resposta: [S]/[N]')).upper()
