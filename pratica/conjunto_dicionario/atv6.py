dicionario = {}

for i in range(3):
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quatidade: "))

    dicionario[nome] = quantidade

print(f'Dicionario de produtos: {dicionario}')

