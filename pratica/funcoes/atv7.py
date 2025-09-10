def uniao(produtos, precos):
    for produto, preco in zip(produtos, precos):
        
        print(f"{produto.strip()}: {preco.strip()}")

produtos = input("Digite os produtos por vírgula: ").split(', ')
precos = input("Digite os preços pro espaço: ").split()

listas_unidas = uniao(produtos, precos)
print(listas_unidas)