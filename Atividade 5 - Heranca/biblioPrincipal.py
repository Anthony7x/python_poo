from biblioteca import Biblioteca, Livro, Revista

l1 = Biblioteca("Dom Casmurro","Machado de Assis", 1899, 310)
l2 = Livro("Dom Casmurro","Machado de Assis",1899, 290)
revist = Revista("Veja","Anthony",1997, 102)

l1.detalhes()
l1.calcularIdadeItem()
l2.verificarTamanho()
revist.verificarEdicao()



