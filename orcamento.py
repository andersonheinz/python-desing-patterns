from typing import Tuple, List
from item import Item


class Orcamento(object):
    def __init__(self) -> None:
        self.__itens: List[Item] = []

    @property
    def valor(self) -> float:
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total

    def obter_itens(self) -> Tuple:
        return tuple(self.__itens)

    @property
    def total_itens(self) -> int:
        return len(self.__itens)

    def adiciona_item(self, item) -> None:
        self.__itens.append(item)
