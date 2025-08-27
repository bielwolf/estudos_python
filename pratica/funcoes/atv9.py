def aplicadesconto (desconto):
    def precofinal(valor):
        return valor - (valor * (desconto /100))
    return precofinal

desconto = float(input("Digite a porcentagem de desconto: "))
valor = float(input("Digite o valor da compra: "))

valor_desconto = aplicadesconto(desconto)
preco_descontado = valor_desconto(valor)

print(f'Preço final com desconto: {preco_descontado}')
