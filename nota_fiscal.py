from datetime import date


class NotaFiscal(object):
    def __init__(
            self,
            razao_social: str,
            cnpj: str,
            itens: int,
            data_de_emissao: date = date.today(),
            detalhes: str = ''
    ) -> None:
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception(
                'Detalhes da nota não pode ter mais do que 20 caracteres'
            )
        self.__detalhes = detalhes
        self.__itens = itens

    @property
    def razao_social(self) -> str:
        return self.__razao_social

    @property
    def cnpj(self) -> str:
        return self.__cnpj

    @property
    def data_de_emissao(self) -> date:
        return self.__data_de_emissao

    @property
    def detalhes(self) -> str:
        return self.__detalhes
