"""
Simulando Strategy utilizando funcoes

"""

from Item import Item
from Orcamento import Orcamento


def ISS(orcamento):
    return ISS.__name__, orcamento.valor * 0.1


def ICMS(orcamento):
    return ICMS.__name__, orcamento.valor * 0.06


class Calculadora_de_impostos(object):
    def realiza_calculo(self, orcamento, calcula_imposto):
        descricao, valor = calcula_imposto(orcamento)
        print(descricao, valor, '%')


if __name__ == '__main__':

    calculador = Calculadora_de_impostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 100))

    calculador.realiza_calculo(orcamento, ISS)
    calculador.realiza_calculo(orcamento, ICMS)
