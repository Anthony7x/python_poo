from funcionario import Funcionario, Engenheiro, Supervisor

f1 = Funcionario("Joana", 3000)
engenheiro1 =  Engenheiro("Anthony", 5100)
supervisor1 = Supervisor("Sampaio", 4500)

f1.informacoes()
engenheiro1.bonusEng()
engenheiro1.informacoes()
supervisor1.relatorio()
