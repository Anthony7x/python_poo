class Biblioteca:
    def __init__(self, titulo, autor, anoPublicacao, numeroPagina):
        self._titulo = titulo
        self._autor  = autor
        self._anoPublicacao = anoPublicacao
        self._numeroPagina = numeroPagina

    def detalhes(self):
        print(f"O Livro escolhido foi {self._titulo} do escritor(a) {self._autor} no ano de {self._anoPublicacao} na qual têm {self._numeroPagina} páginas.")   
        return self._titulo, self._autor, self._anoPublicacao, self._numeroPagina
    
    def calcularIdadeItem(self):
        if self._anoPublicacao <= 1950:
            print(f"O {self._titulo} referente ao ano {self._anoPublicacao} é antigo.")
        elif  self._anoPublicacao >= 1951 and self._anoPublicacao <= 1980:
            print(f"O {self._titulo} referente ao ano {self._anoPublicacao} é recente.")
        elif self._anoPublicacao >= 1981 and self._anoPublicacao <= 2024:
            print(f"O {self._titulo} referente ao ano {self._anoPublicacao} é contemporâneo.")

class Livro(Biblioteca):
    def verificarTamanho(self):
        if self._numeroPagina >= 300:
            print(f"O Livro longo pelo fato de ter {self._numeroPagina}")
        elif self._numeroPagina <= 300:
            print(f"O Livro é curto pelo fato de ter {self._numeroPagina}")

class Revista(Biblioteca):
    def verificarEdicao(self):
        if self._anoPublicacao <= 1998:
            print(f"{self._titulo} do ano {self._anoPublicacao} é uma edição especial.")
        elif self._anoPublicacao >= 1999 and self._anoPublicacao <= 2024:
            print(f"{self._titulo} do ano {self._anoPublicacao} não é uma edição especial.")