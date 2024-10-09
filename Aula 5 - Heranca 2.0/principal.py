from pessoa import Pessoa, Aluno, Professor

pessoa1 = Pessoa("Meuca", 10)
aluno2 = Aluno("Jurandy", 16, 902)
prof1 = Professor("Anderson","20","Programação de aplicativos")

pessoa1.info()

aluno2.info()
aluno2.estudar()
prof1.ensinar()