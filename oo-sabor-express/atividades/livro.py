class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def __str__(self):
        return f'{self.titulo} | {self.autor} | {self.ano_publicacao}'
    
    def emprestar(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis
    

livro1 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)
livro2 = Livro('1984', 'George Orwell', 1949)
Livro.livros = [livro1, livro2]
livro1.emprestar()

print(livro1.disponivel)
print(livro2)
