class Orcamento:
    def __init__(self):
        self.__servicos = []

    def adicionar(self, servico):
        self.__servicos.append(servico)

    def limpar(self):
        self.__servicos.clear()

    def calcular_total(self):
        total = 0
        for servico in self.__servicos:
            total += servico.calcular_preco()
        return total

    def listar(self):
        texto = ""
        for servico in self.__servicos:
            texto += f"{servico.nome}: R$ {servico.calcular_preco():.2f}\n"
        return texto
