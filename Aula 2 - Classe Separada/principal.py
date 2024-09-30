#estamos acessando o arquivo 'pessoa' e dentro desse arquivo estamos importando a classe 'pessoa'
from pessoa import Pessoa

#criando objetos
p1 = Pessoa('João','Correr', 'Rua 90')
p1.exibirHobby()
p1.mudarHobby("Natação")

#Solicitando dados do usuário
nomePessoa = input("Informe o nome da pessoa: ")
hobbyPessoa = input("Informe o hobby da pessoa: ")
endPessoa = input("Qual o endereço? ")

p2 = Pessoa(nomePessoa, hobbyPessoa, endPessoa)
p2.exibirHobby()