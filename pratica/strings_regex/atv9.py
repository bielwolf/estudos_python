import re

livro = input("Digite o nome do livro: ")
letra = input("Digite a letra inicial para pesquisa: ")

palavras = re.findall(rf'\b{letra}[a-zà-ÿ]*', livro, re.IGNORECASE)
print(palavras)  