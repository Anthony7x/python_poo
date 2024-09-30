from livro import  Livro

book =  Livro("Harry Potter", "J.K. Rowling", 2000)
book2 = Livro("O Príncipe", "Maquiavél", 1532)
book.exibirInformacoes()

nomeLivro = input("Informe o nome do livro: ")
autorLivro = input("Informe o autor do livro: ")
anoLivro = int(input("Informe o ano de publicação do livro: "))

book2  = Livro(nomeLivro, autorLivro, anoLivro)
book2.exibirInformacoes()
book2.verificarIdadeLivro()
