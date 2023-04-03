estado = {}
brasil1 = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil1.append(estado.copy())
for e in brasil1:
    print(e)
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')