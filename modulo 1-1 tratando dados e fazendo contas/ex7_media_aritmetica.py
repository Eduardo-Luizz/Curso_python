# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

first = float(input('Digite a primeira nota do aluno: '))
second = float(input('Digite a segunda nota do aluno: '))

print(f'A primeira nota do aluno foi {first :.1f} \nA segunda nota do aluno foi {second :.1f} \nEntão a média dele é {(first + second) / 2 :.1f}')