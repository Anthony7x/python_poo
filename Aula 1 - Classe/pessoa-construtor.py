class Pessoa:
    #Criar o método construtor
    def  __init__(self, nome, altura, idade):
        #Estamos criando os atributos da classe utilizando o método construtor. Nesse caso precisamos passar os parâmetros que serão usados como valores dos atributos.
        self.nome = nome
        self.altura = altura
        self.idade = idade

    #Criando os métodos
    def exibirDados(self):
        print(f"Olá {self.nome}, sua altura é {self.altura} e sua idade é {self.idade} anos")

#Criando os objetos
p1 = Pessoa("Jack Frosty", 1.87, 18)
p2 = Pessoa("Negão da BL", 1.89, 20)
p3 = Pessoa("Catia Blazer", 1.57, 25)

p1.exibirDados()
p2.exibirDados()
p3.exibirDados()
