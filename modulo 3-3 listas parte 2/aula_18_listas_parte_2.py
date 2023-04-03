teste = list()
teste.append('Eduardo')
teste.append(22)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 21
galera.append(teste[:]) # sem isso ficara maria 22 nas duas posições
print(galera)


galeras = [['Joao', 21], ['Ana', 35], ['Jeni', 24], ['José', 45]]
print(galeras)
print(galeras[0])
print(galeras[0][0])
print(galeras[2][1])
for pessoa in galeras:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')

pessoas = list()
dados = list()
totmai = totmen = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()
print(pessoas)

for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'temos {totmai} maiores e {totmen} menores de idade')
