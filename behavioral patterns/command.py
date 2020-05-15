"""
# Command
Abstrair um comando que deve ser executado, pois não é possível executá-lo
naquele momento (pois precisamos por em uma fila ou coisa do tipo).
E usado quando temos que separar os comandos que serão executados do objeto que
ele pertence.

"""

from datetime import date
from abc import ABCMeta, abstractmethod


class Pedido(object):

    def __init__(self, cliente: str, valor: float) -> None:
        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_finalizacao = None

    def paga(self) -> None:
        self.__status = 'PAGO'

    def finaliza(self) -> None:
        self.__data_finalizacao = date.today()
        self.__status = 'ENTREGUE'

    @property
    def cliente(self) -> str:
        return self.__cliente

    @property
    def valor(self) -> float:
        return self.__valor

    @property
    def status(self) -> str:
        return self.__status

    @property
    def data_finalizacao(self) -> date:
        return self.__data_finalizacao


class FilaDeTrabalho(object):

    def __init__(self) -> None:
        self.__comandos = []

    def adiciona(self, comando) -> None:
        self.__comandos.append(comando)

    def processa(self) -> None:
        for comando in self.__comandos:
            comando.executa()


class Comando(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def executa(self) -> None:
        pass


class ConcluiPedido(Comando):

    def __init__(self, pedido) -> None:
        self.__pedido = pedido

    def executa(self) -> None:
        self.__pedido.finaliza()


class PagaPedido(Comando):

    def __init__(self, pedido) -> None:
        self.__pedido = pedido

    def executa(self) -> None:
        self.__pedido.paga()


if __name__ == '__main__':

    pedido1 = Pedido('Anderson', 150.31)
    pedido2 = Pedido('Heinz', 250.32)

    fila_de_trabalho = FilaDeTrabalho()
    fila_de_trabalho.adiciona(PagaPedido(pedido1))
    fila_de_trabalho.adiciona(PagaPedido(pedido2))
    fila_de_trabalho.adiciona(ConcluiPedido(pedido1))
    fila_de_trabalho.processa()
    print(fila_de_trabalho)
