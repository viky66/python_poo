class Funcionario:
    def __init__(self, cargo, salario = 2000):
        self.__cargo = cargo
        self.__salario = salario #esse atributo está opcional, caso nao seja informado um valor padrao de R$2000

    def getCargo(self): #set altera insere e get retorna o conteudo
        return self.__cargo
    
    def setCargo(self, novoCargo): #2 metodos 
        self.__cargo = novoCargo

#iremos utilizar uma forma unica do python para acessar atributos privados
    #criando o 'get' do salário
    @property #esse elemento irá criar um get 'mais amigável'
    def salario(self):
        return self.__salario
    
    @salario.setter #irá criar um set para o salário 'mais amigavel'
    def salario(self, valor):
        if valor <= 0:
            print("Informe o valor positivo")
        else:
            self.__salario = valor