"""
O exemplo abaixo e um recurso padrao da linguagem, o designer pattern decorator aplica o mesmo conceito na OO, porem
com mais flexibilidade.

"""

def TDA(metodo_ou_funcao):
    def wrapper(*args, **kwargs):
        return metodo_ou_funcao(*args, **kwargs) + 20.0
    return wrapper

def TDE(metodo_ou_funcao):
    def wrapper(*args, **kwargs):
        return metodo_ou_funcao(*args, **kwargs) + 50.0
    return wrapper


@TDE
@TDA
def valor_sem_taxas(valor):
    return valor


if __name__ == '__main__':
    valor_total = valor_sem_taxas(100)
    print(valor_total)