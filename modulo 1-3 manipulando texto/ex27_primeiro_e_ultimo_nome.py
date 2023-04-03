# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

full_name = str(input('Digite seu nome: ')).strip()
partial_name = full_name.split()
print(f'Seu nome completo é {full_name} \nSeu primeiro nome é {partial_name[0]} \nSeu último nome é {partial_name[-1]}')