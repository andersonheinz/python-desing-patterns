"""
# Template Method
Diferentes algoritimos com estruturas parecidas
Cada classe com sua responsabilidade separada
A classe mãe controla os filhos.
Os filhos preenchem apenas as lacunas da mãe, aquele métodos abstratos, mas a classe mãe está no poder e chama estes métodos dos filhos.
Esse fato que filhos não ficam mais no controle da execução também é chamado de The Hollywood Principle.

"""

from abc import ABCMeta, abstractmethod
from Item import Item
from Orcamento import Orcamento


class Template_de_imposto_condicional(object):
    __metaclass__ = ABCMeta

    def calcula(self, orcamento):

        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass


class ICPP(Template_de_imposto_condicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05


class IKCV(Template_de_imposto_condicional):

    def deve_usar_maxima_taxacao(self, orcamento):

        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self, orcamento):

        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False


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

    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())
