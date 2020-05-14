"""
Utilizando parametros nomeados para obter o mesmo efeito do builder

"""

from datetime import date
from Item import Item
from Nota_fiscal import Nota_fiscal


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

    nota_fiscal = Nota_fiscal(
        cnpj='012345678901234',
        razao_social='FHSA Limitada',
        itens=itens
    )

    print(nota_fiscal)
