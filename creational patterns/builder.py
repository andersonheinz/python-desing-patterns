"""

# Builder
Utilizar quando o objeto for complexo e com logica complicada, porem pode ser resolvido com parametros nomeados,
conforme arquivo builder_simulacao.py

"""

from datetime import date
from Item import Item
from Nota_fiscal import Nota_fiscal


class Criador_de_nota_fiscal(object):

    def __init__(self):

        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = None
        self.__itens = None
        self.__detalhes = None

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_data_de_emissao(self, data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self

    def com_itens(self, itens):
        self.__itens = itens
        return self

    def com_detalhes(self, detalhes):
        self.__detalhes = detalhes
        return self

    def constroi(self):

        if self.__razao_social is None:
            raise Exception('Razão Social deve ser preenchida')
        if self.__cnpj is None:
            raise Exception('CNPJ deve ser preenchido')
        if self.__itens is None:
            raise Exception('Itens deve ser preenchido')
        if self.__data_de_emissao is None:
            self.__data_de_emissao = date.today()
        if self.__detalhes is None:
            self.__detalhes = ''

        return Nota_fiscal(razao_social=self.__razao_social,
                           cnpj=self.__cnpj, data_de_emissao=self.__data_de_emissao,
                           itens=self.__itens, detalhes=self.__detalhes
                           )


if __name__ == '__main__':

    itens=[
        Item(
            'ITEM A',
            100
        ),
        Item(
            'ITEM B',
            200
        )
    ]

    nota_fiscal_criada_com_builder = (Criador_de_nota_fiscal()
                                    .com_razao_social('FHSA Limitada')
                                    .com_cnpj('012345678901234')
                                    .com_itens(itens)
                                    .constroi())

    print(nota_fiscal_criada_com_builder)


