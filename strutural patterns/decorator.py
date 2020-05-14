"""
# Decorator
Comportamentos compostos por outras classes da mesma hierarquia.

"""

from Item import Item
from Orcamento import Orcamento
from abc import abstractmethod


class Imposto(object):

    def __init__(self, outro_imposto=None):
        self.__outro_imposto = outro_imposto

    def calculo_do_outro_imposto(self, orcamento):

        if self.__outro_imposto is None:
            return 0
        else:
            return self.__outro_imposto.calcula(orcamento)

    @abstractmethod
    def calcula(self, orcamento):
        pass


class ISS(Imposto):

    def calcula(self, orcamento):
        return orcamento.valor * 0.1 + self.calculo_do_outro_imposto(orcamento)


class ICMS(Imposto):

    def calcula(self, orcamento):
        return orcamento.valor * 0.06 + self.calculo_do_outro_imposto(orcamento)


class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)

        print(imposto_calculado)


if __name__ == '__main__':

    calculador = Calculador_de_impostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 100))
    orcamento.adiciona_item(Item('ITEM 3', 50))

    print('ISS com ICMS')
    calculador.realiza_calculo(orcamento, ISS(ICMS()))

