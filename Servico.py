class Servico:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def calcular_preco(self):
        raise NotImplementedError("Cada serviço deve calcular seu preço")
