# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

name = str(input('Digite um nome: ')).strip().upper()

print(f"O nome digitado foi {name} \nPossui SILVA no nome: {'SILVA' in name}")
