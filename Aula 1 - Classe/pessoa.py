class Pessoa:
    #atributos
    nome = "Anthony"
    peso = 18
    escolaridade = "Ensino Técnico e Superior"

    #métodos
    def falar(self, texto):
        print(f"Tenho algo para te dizer: {texto}")

#Criando os Objetos
pessoa1 = Pessoa()
print(pessoa1.nome)
pessoa1.falar("Boa tarde, hoje é segunda-feira")
