"""
# Strategy

Temos conjunto de algoritmos similares, e precisamos alternar entre eles em
diferentes pedaços da aplicação.
Podemos usar o Duck Typing passando a instância dos objetos que representam
nossos impostos como parâmetro no lugar de uma função.

"""

from Item import Item
from Orcamento import Orcamento


class ICMS(object):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06

    def descricao(self):
        return type(self).__name__


class ISS(object):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1

    def descricao(self):
        return type(self).__name__


class CalculadoraDeImpostos(object):
    # Strategy
    def realiza_calculo(self, orcamento, imposto):
        # Duck Typing
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto.descricao(), imposto_calculado, '%')


if __name__ == '__main__':

    calculador = CalculadoraDeImpostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 100))

    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())
