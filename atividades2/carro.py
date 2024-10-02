class Carro:
    #criando o metodo construtor
    def __init__(self, marca, modelo, ano, precoDiario):
        #passando os parametros que serao usados como valores do atributo
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.precoDiario = precoDiario

    def exibirDetalhes(self):
        print(f"Olá, a marca do seu carro é {self.marca}, o seu modelo é {self.modelo}, do ano {self.ano} e seu preço diário é de {self.precoDiario}")

    def calcularPrecoAluguel(self, dias):
        total = dias * self.precoDiario
        return total




