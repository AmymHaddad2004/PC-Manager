from Servico import Servico


class ServicoPorHora(Servico):
    def __init__(self, nome, valor_hora, horas):
        super().__init__(nome)
        self.__valor_hora = valor_hora
        self.__horas = horas

    def calcular_preco(self):
        return self.__valor_hora * self.__horas
