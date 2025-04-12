# crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# transfira todas as funções utilizadas nos ex: 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando

from utilidades_cev import moeda

valor = float(input("Digite o preço: R$"))

moeda.resumo(valor)