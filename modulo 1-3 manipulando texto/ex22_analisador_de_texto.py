# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

name = str(input('Digite seu nome: ')).strip()
first = name.split()
print(f'Maiúscula: {name.upper()}')
print(f'Minúscula: {name.lower()}')
print(f"Total de letras: {len(name) - name.count(' ')}")
print(f'Seu primeiro nome é {first[0]}')
