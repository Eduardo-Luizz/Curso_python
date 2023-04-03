#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite sua frase: ')).lower().strip()
total_a = frase.count('a')
ultima_ocorrencia = frase.rfind('a')
primeira_ocorrencia = frase.index('a')
print(f"A letra 'a' aparece {total_a} vezes \nA última ocorrência está na {ultima_ocorrencia + 1} posição \nA primeira ocorrência está na {primeira_ocorrencia + 1} posição")
