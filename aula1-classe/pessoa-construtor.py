class Pessoa:
    #criando o metodo construtor
    def __init__(self, nome, hobby, endereco):
        # estamos criando atributos da classe utilizando o metodo construtor. Nesse caso precisamos passar os parametros que serao usados como valores do atributo
        self.nome = nome
        self.hobby = hobby
        self.endereco = endereco

    #criando os métodos normais
    def exibirDados(self):
        print(f"Olá, {self.nome} seu hobby é {self.hobby} e seu endereço é {self.endereco}")
    
#criando os objetos 
pessoal = Pessoa("geraldo", "corredor", "rua 10 cohab")
pessoal.exibirDados() #chamado o metodo da classe

pessoa2 = Pessoa("Karla", "artes marciais", "av. 12 Renascença")
print(pessoa2.nome)
