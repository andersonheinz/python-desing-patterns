"""
Utilizando parametros nomeados para obter o mesmo efeito do builder

"""


from item import Item
from nota_fiscal import NotaFiscal


if __name__ == '__main__':

    itens = [
        Item(
            'ITEM A',
            100
        ),
        Item(
            'ITEM B',
            200
        )
    ]

    nota_fiscal = NotaFiscal(
        cnpj='012345678901234',
        razao_social='FHSA Limitada',
        itens=itens
    )

    print(nota_fiscal)
