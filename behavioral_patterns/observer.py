"""
# Observer
Quando o acoplamento da nossa classe está crescendo, ou quando temos diversas
ações diferentes a serem executadas após um determinado processo. Nestes casos,
podemos implementar o Observer.

"""

from datetime import date
from Item import Item


def envia_por_email(nota_fiscal):
    print('enviando nota por e-mail...')


def salva_no_banco(nota_fiscal):
    print('salvando no banco...')


def imprime(nota_fiscal):
    print('imprimindo ...')


class NotaFiscal(object):
    def __init__(
            self,
            razao_social,
            cnpj,
            itens,
            data_de_emissao=date.today(),
            detalhes='',
            observadores=[]):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception('Detalhe da nota superior à 20 caracteres!')
        self.__detalhes = detalhes
        self.__itens = itens

        for observador in observadores:
            observador(self)

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes


if __name__ == '__main__':

    itens = [
        Item(
            nome='ITEM A',
            valor=100
        ),
        Item(
            nome='ITEM B',
            valor=200
        )
    ]

    nota_fiscal = NotaFiscal(
        cnpj='012345678901234',
        razao_social='FHSA Limitada',
        itens=itens,
        observadores=[envia_por_email, salva_no_banco, imprime]
    )
