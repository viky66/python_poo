from pessoa import Pessoa, Aluno, Professor

pessoa1 = Pessoa("Getulio", 65)
aluno1 = Aluno("Keila", 20, "2ª ensino médio")

pessoa1.info()

aluno1.info()
aluno1.estudar()

professor1 = Professor("Roberto", 40, "matemática")
professor1.ensinar()