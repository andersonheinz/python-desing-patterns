class Item(object):
    def __init__(self, nome: str, valor: float) -> None:
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self) -> float:
        return self.__valor

    @property
    def nome(self) -> str:
        return self.__nome
