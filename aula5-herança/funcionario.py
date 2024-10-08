class Pessoa: #super-classe ou classe mae
    def __init__(self, nome, cargo):
        #mudando a visibilidade do atributo privado para publico
        self._nome = nome
        self._cargo = cargo

    def informacoes(self): 
        print(f"Olá {self._nome}, na empresa, seu cargo é: {self._cargo}")

#criando classe  filha
class Engenheiro(Pessoa): # a classe engenheiro está herdando as caracteristicas da classe Pessoa, que será sua classe mãe
    def mostrarDetalhes(self):
        print(f"Olá, eu sou {self._nome} e sou engenheiro")


class Secretario(Pessoa):

    def relatorio(self): 
        print(f"Olá {self._nome}, seja bem-vindo à empresa, o seu cargo é {self._cargo}")
