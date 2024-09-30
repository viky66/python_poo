#estamos acessando o arquivo 'pessoa' e dentro o arquivo estamos importando a classe 'pessoa'
from pessoa import Pessoa

#criando os objetos
p1 = Pessoa("César", 49, "Lasanha")
p2 = Pessoa("Livia", 31, "Churrasco")

p1.mostrarComida()
p2.mostrarComida()