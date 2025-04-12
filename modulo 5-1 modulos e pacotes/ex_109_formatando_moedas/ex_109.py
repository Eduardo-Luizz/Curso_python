# modifique as funções que foram criadas no ex-107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não
#formatado pela função moeda(), desenvolvido no ex-108

import moeda

valor = float(input("Digite o preço: R$"))

moeda.moeda(valor, 10)