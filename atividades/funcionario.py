class Funcionario:
    #criando o metodo construtor
    def __init__(self, nome, cargo, salario):
        #passando os parametros que serao usados como valores do atributo
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibirDados(self):
        print(f"Olá, {self.nome} o seu cargo é {self.cargo} e seu salário é de {self.salario}")

    def verificaSalario(self):
        if self.salario <= 2000:
            print(f"{self.nome}: Você tem direito a bônus!")
        else:
            print(f"{self.nome}: Você não tem direito a bônus")