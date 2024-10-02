class Conta:
    #construtor
    def __init__(self, numero, titular, saldo, limite): #estamos apssando um valor padrao para o limite, tornando-o opcional, dessa forma o objeto ao ser criado pode ter um limite informado ou nao
        self.__numero = numero  #_ protação, 2 anderlines antes do nome indica que esse atributo está com visibilidade "privado", o contrario significa que está "público"
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #demais metodos 
    def detalhes(self):
        print(f"Olá {self.__titular}, seu saldo atual é {self.__saldo}")

    #método que irá retornar o conteúdo do limite
    def getLimite(self):
        return self.__limite
        
    #metodo que irá alterar o valor do limite 
    def setLimite(self, valor):
        if valor < 0:
            print("Informe um valor positivo para o limite")
        else:
            self.__limite = valor

    #método para depositar valores
    def depositar(self, valor):
        if valor < 0:
            print("Informe um valor maior que zero")
        else: self.__saldo = self.__saldo + valor

    #método para sacar valor
    def sacar(self, valor):
        if self.__saldo <= 0 or valor > self.__saldo:
            print("Saldo insuficiente")
        else:
            self.__saldo = self.__saldo - valor