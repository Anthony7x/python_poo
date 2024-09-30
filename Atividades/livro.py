class Livro:
    def  __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def exibirInformacoes(self):
        print(f"O Livro escolhido foi {self.titulo}, do autor {self.autor} onde o livro foi publicado no ano de {self.ano_publicacao}.")
        
    def verificarIdadeLivro(self):
        if self.ano_publicacao <= 1974:
            print(f"O livro {self.titulo} é um clássico.")
        else:
            print("Ainda não é considerado um clássico.")
        
