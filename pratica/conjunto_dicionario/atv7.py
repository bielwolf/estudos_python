estoque = { 
    "Caderno universitário": 50, 
    "Caneta azul": 120, 
    "Borracha branca": 30 
} 

nome = input("Nome do produto a ser atualizado: ")
qtd = int(input("Nova quantidade: "))

if nome in estoque:
    estoque[nome] = qtd
    print('Quantidade atualizada com sucesso!')
    print(estoque)
else:
    print('Produto não encontrado')