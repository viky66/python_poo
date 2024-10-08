from funcionario import Funcionario

Funcionario1 = Funcionario("Gerente",3000)
print("Seu cargo atual é: ", Funcionario1.getCargo())

#tentando mudar o valor do atributo
Funcionario1.__cargo = "Supervisor" #acessando o atributo direto 
Funcionario1.setCargo("Engenheiro") #acessando o método para mudar o cargo
print("Seu cargo atual é: ", Funcionario1.getCargo())

#exibindo o salario
print("O seu salário atual é ", Funcionario1.salario)


Funcionario1.salario = -5000
print("O seu salário atual é ", Funcionario1.salario)