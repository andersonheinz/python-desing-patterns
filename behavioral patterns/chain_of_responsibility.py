"""
# Chain of Responsibility
E quebrado as responsabilidades em várias diferentes classes, e as unido como uma corrente.
Utilizar quando temos uma lista de comandos a serem executados de acordo com algum cenário em específico, e sabemos
também qual o próximo cenário que deve ser validado, caso o anterior não satisfaça a condição.

"""

from Item import Item
from Orcamento import Orcamento


class Desconto_por_cinco_itens(object):

    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        else:
            return self.__proximo_desconto.calcula(orcamento)


class Desconto_por_mais_de_quinhentos_reais(object):

    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return self.__proximo_desconto.calcula(orcamento)


class Sem_desconto(object):

    def calcula(self, orcamento):
        return 0


class Calculador_de_descontos(object):

    def calcula(self, orcamento):
        desconto = Desconto_por_cinco_itens(
                   Desconto_por_mais_de_quinhentos_reais(
                   Sem_desconto()
                   )
        ).calcula(orcamento)
        return desconto


if __name__ == '__main__':

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 100))
    orcamento.adiciona_item(Item('ITEM - 2', 50))
    orcamento.adiciona_item(Item('ITEM - 3', 400))

    calculador = Calculador_de_descontos()

    desconto = calculador.calcula(orcamento)

    print('Desconto calculado %s' % (desconto))