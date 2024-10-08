from funcionario import Pessoa, Engenheiro, Secretario

f1 = Pessoa("Joana", "Gerente")
engenheiro1 = Engenheiro("Roberto", "Engenheiro Pleno")

f1.informacoes()
engenheiro1.informacoes()
engenheiro1.mostrarDetalhes()



secretario = Secretario("Victoria", "Supervisor Geral")

secretario.relatorio()