from livro import Livro

livro3 = Livro('Harry Potter e a Pedra Filosofal', 'J.K', 1997)
livro3.emprestar()
print(livro3.disponivel)

ano_especifico = 1954
livro_disponivel = Livro.verificar_disponibilidade(1954)
print (livro_disponivel)
