from Servico import Servico


class ServicoFixo(Servico):
    def __init__(self, nome, preco):
        super().__init__(nome)
        self.__preco = preco

    def calcular_preco(self):
        return self.__preco
