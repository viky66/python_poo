class Pessoa:
    #Atributos
    nome = "vic"
    idade = "25"
    altura = "1.60"

    #métodos - são os comportamentos da classe 
    def falar (self,texto): #self é um parametro obrigatorio do python que informa que o método pertence à própria classe que foi criada
        print(f"Tenho algo para te falar: {texto}")

#criando objetos 
pessoal = Pessoa() #dessa forma estamos criando um objeto do tipo pessoa

print(pessoal.nome, pessoal.idade)
pessoal.falar("Bom dia, hoje é segunda-feira")