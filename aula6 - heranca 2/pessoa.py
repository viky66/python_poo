class Pessoa: #super classe ou classe mãe
    def __init__(self, nome, idade): #protegido - externo nao consegue acessar, apenas um _
        self._nome = nome
        self._idade = idade

    def info(self):
        print(f"Nome: {self._nome}. Idade: {self._idade}")

#Classe filha 1 - Aluno
class Aluno(Pessoa): #pass informa que vai ter algum conteudo
    def __init__(self, nome, idade, serie):
         super().__init__(nome, idade) #chamando o metodo construtor da classe mae
         self._serie = serie # utilizando um atributo exclusivo da classe filha

    def estudar(self):
        print(f"{self._nome}, está estudando na série {self._serie}")

#Classe filha 2 - Professor
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self._disciplina = disciplina
    def ensinar(self):
        print(f"{self._nome}, o professor(a) da disciplina de {self._disciplina}, está ensinando")