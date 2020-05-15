"""
# Decorator
Comportamentos compostos por outras classes da mesma hierarquia.

"""

from item import Item
from orcamento import Orcamento
from abc import ABCMeta, abstractmethod


class Imposto(object):
    def __init__(self, outro_imposto=None) -> None:
        self.__outro_imposto = outro_imposto

    def calculo_do_outro_imposto(self, orcamento):
        if self.__outro_imposto is None:
            return 0
        else:
            return self.__outro_imposto.calcula(orcamento)

    @abstractmethod
    def calcula(self, orcamento):
        pass


class TemplateDeImpostoCondicional(Imposto):
    __metaclass__ = ABCMeta

    def calcula(self, orcamento):

        if self.deve_usar_maxima_taxacao(orcamento):
            return (
                self.maxima_taxacao(orcamento) +
                self.calculo_do_outro_imposto(orcamento)
            )
        else:
            return (
                self.minima_taxacao(orcamento) +
                self.calculo_do_outro_imposto(orcamento)
            )

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass


class ICPP(TemplateDeImpostoCondicional):
    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05


class IKCV(TemplateDeImpostoCondicional):
    def deve_usar_maxima_taxacao(self, orcamento):

        return (
            orcamento.valor > 500 and
            self.__tem_item_maior_que_100_reais(orcamento)
        )

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self, orcamento):

        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False


class CalculadorDeImpostos(object):
    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)

        print(imposto_calculado)


if __name__ == '__main__':

    calculador = CalculadorDeImpostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 100))
    orcamento.adiciona_item(Item('ITEM 3', 50))

    print('ICPP com IKCV')
    calculador.realiza_calculo(orcamento, ICPP(IKCV()))
