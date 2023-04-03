#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

city = str(input('Digite o nome de uma cidade: ')).strip().upper()

print(f"O nome digitado foi {city} \nPossui SANTO no nome: {city[:5] == 'SANTO'}")
