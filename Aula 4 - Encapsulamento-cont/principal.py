from funcionario import Funcionario

funcionario1 = Funcionario("Ketlen", 3000)

print(funcionario1.getNome())

funcionario1.setNome("Kaio")
print(funcionario1.getNome())

print("Seu nome atual é ", funcionario1.getNome())

#Estamos tentando acessar o atributo salario
print("Seu salário atual é: ", funcionario1.salario)

funcionario1.salario = 5000

print("Seu salário atual é: ", funcionario1.salario)